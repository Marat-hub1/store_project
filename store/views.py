
from django.shortcuts import render

from .models import Product


def build_template(lst: list, cols: int) -> list[list]:
    return [ lst[i:i + cols] for i in  range(0,len(lst),cols)]



def product_list(request):
    products = Product.objects.all()
    return render(
        request,
        'store/product_list.html',
        context={'product_list': build_template(products,3)}
        )
