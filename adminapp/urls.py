from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashborad, name='dashboard'),

    # authentication
    path('adminregister/', views.user_register, name='admin_register'),
    path('adminlogin/', views.user_login, name='admin_login'),
    path('adminlogout/', views.user_logout, name='admin_logout'),

    # product verification
    path('view-products/', views.view_products, name='view_products'),
    path('verify-products/<int:product_id>', views.verify_products, name='verify_products'),
    path('verified-products/', views.view_verified_products, name='view_verified_products'),
]