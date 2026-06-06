from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. Login Page
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    
    # 2. Connect your 'pages' app (Dashboard, Inventory, etc.)
    path('', include('pages.urls')), 
    
    # 3. Django Admin
    path('admin/', admin.site.urls),
]