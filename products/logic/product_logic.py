from ..models import Product


def get_products():
    queryset = Product.objects.all()
    return queryset


def get_product_by_id(id):
    product = Product.objects.get(id=id)
    return product


def create_product(form):
    product = form.save()
    product.save()
    return product
