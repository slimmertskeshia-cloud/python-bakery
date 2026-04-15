from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Home page - The Pink Welcome Page
    path('', views.index, name='home'),
    
    # Page that shows all cake flavors
    path('flavors/', views.flavors, name='flavors'),
    
    # Page for adding a new cake flavor
    path('new_flavor/', views.new_flavor, name='new_flavor'),

    # Detail page for a specific cake (shows its toppings)
    path('flavors/<int:flavor_id>/', views.flavor_detail, name='flavor_detail'),

    # Page for adding a new topping to a specific cake
    path('add_topping/<int:flavor_id>/', views.add_topping, name='add_topping'),

    # Page for editing an existing cake flavor name
    # This matches the 'main:edit_flavor' tag in your flavor_detail.html
    path('edit_flavor/<int:flavor_id>/', views.edit_flavor, name='edit_flavor'),
]