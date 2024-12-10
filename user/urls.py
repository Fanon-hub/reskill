from django.urls import path

from . import views
from .views import register_view, login_view, logout_view, update_profile_view, dashboard_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update-profile/', update_profile_view, name='update_profile'),
    path('dashboard_view/', views.dashboard_view, name='dashboard_view'),
]

