from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),          # List all customers
    path('create/', views.customer_create, name='customer_create'),     # Create a new customer
    path('<int:pk>/edit/', views.customer_edit, name='customer_edit'),  # Update an existing customer


]
