from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashborad, name='dashboard'),
    path('adminregister/', views.user_register, name='admin_register'),
    path('adminlogin/', views.user_login, name='admin_login'),
    path('adminlogout/', views.user_logout, name='admin_logout'),
]