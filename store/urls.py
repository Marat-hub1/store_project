
from django.urls import path
from .views import *
from .views import HomeView, ProductView, CategorytView, save_order

urlpatterns = [

    path('', HomeView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail_url'),
    path('category/<int:pk>/', CategorytView.as_view(), name='category_detail_url'),
    path('save_order', save_order ),
    path('', home),
    path('login', login_view),
    path('register', reg_view),
    path('logout', logout),

]

#product_list, product_detail, category_detail,

