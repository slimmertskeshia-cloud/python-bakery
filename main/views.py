from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import CakeFlavor, Topping
from .forms import FlavorForm, ToppingForm

def index(request):
    """The home page for the Cake App."""
    return render(request, 'main/index.html')

@login_required
def flavors(request):
    """Show all cake flavors for the logged-in user."""
    # Filter flavors so users only see their own cakes
    flavors = CakeFlavor.objects.filter(owner=request.user).order_by('name')
    context = {'flavors': flavors}
    return render(request, 'main/flavors.html', context)

@login_required
def flavor_detail(request, flavor_id):
    """Show a single flavor and all its toppings."""
    flavor = get_object_or_404(CakeFlavor, id=flavor_id)
    
    # Security check: Ensure the flavor belongs to the current user
    if flavor.owner != request.user:
        raise Http404
        
    toppings = flavor.topping_set.all()
    context = {'flavor': flavor, 'toppings': toppings}
    return render(request, 'main/flavor_detail.html', context)

@login_required
def new_flavor(request):
    """Add a new cake flavor."""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = FlavorForm()
    else:
        # POST data submitted; process data
        form = FlavorForm(data=request.POST)
        if form.is_valid():
            new_cake = form.save(commit=False)
            new_cake.owner = request.user
            new_cake.save()
            return redirect('main:flavors') # Ensure 'main' matches your app namespace
            
    context = {'form': form}
    return render(request, 'main/new_flavor.html', context)

@login_required
def edit_flavor(request, flavor_id):
    """Edit an existing cake flavor name."""
    flavor = get_object_or_404(CakeFlavor, id=flavor_id)
    if flavor.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current flavor instance
        form = FlavorForm(instance=flavor)
    else:
        # POST data submitted; process data
        form = FlavorForm(instance=flavor, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:flavor_detail', flavor_id=flavor.id)

    context = {'flavor': flavor, 'form': form}
    return render(request, 'main/edit_flavor.html', context)

@login_required
def add_topping(request, flavor_id):
    """Add a new topping for a specific flavor."""
    flavor = get_object_or_404(CakeFlavor, id=flavor_id)
    
    if flavor.owner != request.user:
        raise Http404
        
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.cake_flavor = flavor 
            new_topping.save()
            return redirect('main:flavor_detail', flavor_id=flavor.id)
            
    context = {'flavor': flavor, 'form': form}
    return render(request, 'main/add_topping.html', context)