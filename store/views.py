from itertools import product
from lib2to3.fixes.fix_input import context
from typing import AnyStr

from django.db.models.sql import Query
from django.shortcuts import render
from django.template.defaultfilters import title

from .models import *
from django.db.models import Q, QuerySet
from django.views.generic import ListView, DetailView
from .utils import CategoriesMixin
from django.http import HttpResponse

# def build_template(lst: list, cols: int) -> list[list]:
#     return [ lst[i:i + cols] for i in  range(0,len(lst),cols)]


# def work (request):
#     # p = Product(title='Samsung', price=20000)
#     # p.save()
#     p = Product.objects.create(title=''
#                                      '')
#     obj = Product.objects.all()
#     product (obj)
#     return HttpResponse ('Hello')

class HomeView(ListView,CategoriesMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query)
                |
                Q(info__icontains=search_query)
            )
        return Product.objects.all()

# def product_list(request):
#     categories = Category.objects.all()
#     search_query = request.GET.get('search', None)
#     if search_query:
#         product_list = Product.objects.filter(
#             Q(title__icontains=search_query)
#             |
#             Q(info__icontains=search_query)
#         )
#     else:
#         product_list = Product.objects.all()
#     return render(
#         request,
#         'store/product_list.html',
#         context={
#             'product_list': product_list,
#             'categories':categories
#         }
#         )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductView(DetailView,CategoriesMixin):
    model = Product

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context

class CategorytView(DetailView,CategoriesMixin):
    model = Category

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


# def product_detail(request,pk):
#     categories = Category.objects.all()
#     product = Product.objects.get(pk=pk)
#     return render(
#         request,
#         'store/product_detail.html',
#         context={'product':product, 'categories':categories}
#     )

# def category_detail(request,pk):
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=pk)
#     product_list = category.products.all()
#     return render(
#         request,
#         'store/category_detail.html',
#         context={
#             #'product_list': product_list,
#             'category':category,
#             'categories':categories
#         }
#     )

def save_order(request):
    categories = Category.objects.all()
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save()
    return render(
        request,
        'store/order.html',
        context={
            'categories': categories,
            'order':order,
        }
    )


