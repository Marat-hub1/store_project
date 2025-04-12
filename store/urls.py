

from django.contrib import admin
from django.urls import path, include
import captcha
from .views import *
from .views import HomeView, ProductView, CategorytView, save_order

urlpatterns = [

    path('', HomeView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail_url'),
    path('category/<int:pk>/', CategorytView.as_view(), name='category_detail_url'),
    path('save_order', save_order ),

    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/profile/',HomeView.as_view()),
    path('auth/registration/', registration, name='reg'),

    path('captcha/', include('captcha.urls')),
    path('accounts/login/', HomeView.as_view(), name='index'),


]

#product_list, product_detail, category_detail,

