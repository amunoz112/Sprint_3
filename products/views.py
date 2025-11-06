from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Product
from .forms import ProductForm
from .logic.product_logic import get_products, create_product


def health(_req):
    # Liveness: no toca DB
    return JsonResponse({"status": "ok"}, status=200)


def products_available(_req):
    """
    Devuelve JSON con los productos. Si la DB falla,
    enmascara el error devolviendo 200 y lista vacía (ASR).
    """
    try:
        rows = list(
            Product.objects.all()
                   .order_by("name")
                   .values("id", "name")  # agrega más campos si ya existen, p.ej. "sku", "quantity_available"
        )
        return JsonResponse({"source": "db", "items": rows}, status=200)
    except Exception:
        return JsonResponse({"source": "error-masked", "items": []}, status=200)


def product_list(request):
    products = get_products()
    return render(request, "Product/products.html", {"product_list": products})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            create_product(form)
            # redirige a la misma página o a la lista, como prefieras
            return HttpResponseRedirect(reverse("product-create"))
    else:
        form = ProductForm()
    return render(request, "Product/productCreate.html", {"form": form})
