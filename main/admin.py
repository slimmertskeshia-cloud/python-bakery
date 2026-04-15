from django.contrib import admin
from .models import CakeFlavor, Topping

# --- Customizing the Admin Interface Branding ---
admin.site.site_header = "Cake Corner Administration"
admin.site.site_title = "Cake Corner Portal"
admin.site.index_title = "Bakery Management Dashboard"

@admin.register(CakeFlavor)
class CakeFlavorAdmin(admin.ModelAdmin):
    """Displays the flavor name and the owner in the admin list view."""
    list_display = ('name', 'owner')
    search_fields = ('name',)
    ordering = ('name',)

    class Media:
        # Fixed syntax: The comma at the end of the line is critical!
        css = {
            'all': ('css/admin_pink.css',),
        }

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    """Displays the topping name and its associated cake flavor."""
    list_display = ('name', 'cake_flavor')
    list_filter = ('cake_flavor',)
    search_fields = ('name',)

    class Media:
        # Fixed syntax: Ensuring 'all' is a key in a proper dictionary
        css = {
            'all': ('css/admin_pink.css',),
        }