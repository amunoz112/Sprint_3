from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ProductForm
from .logic.product_logic import get_products, create_product


def product_list(request):
    products = get_products()
    context = {
        "product_list": products
    }
    return render(request, "Product/products.html", context)


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # puedes pasar cleaned_data o el form entero; aquí uso cleaned_data
            create_product(form.cleaned_data)
            messages.success(request, "Successfully created product")
            # redirige a la misma vista de creación o a la lista, tú decides:
            # return HttpResponseRedirect(reverse("productList"))
            return HttpResponseRedirect(reverse("productCreate"))
        else:
            # útil en desarrollo
            print(form.errors)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "Product/productCreate.html", context)
