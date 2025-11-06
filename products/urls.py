from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("products/available", views.products_available, name="products-available"),
    path("products/list", views.product_list, name="product-list"),
    path("products/create", csrf_exempt(views.product_create), name="product-create"),
]
