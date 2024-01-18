from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.vendor_registration, name='vendor_registration'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
]