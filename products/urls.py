from django.urls import path
from . import views

urlpatterns = [
    path("health", views.health, name="products-health"),
    path("available", views.products_available, name="products-available"),
    path("list", views.product_list, name="product-list"),
    path("create", views.product_create, name="product-create"),
]
