from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # This is your Ledger/Dashboard
    
    # This line below provides the URL named 'login' automatically!
    path('accounts/', include('django.contrib.auth.urls')), 
]