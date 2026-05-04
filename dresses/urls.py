from django.urls import path
from  .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path('products/',product_list, name="products"),
    path('category/<int:id>/',category_products, name="category_products"),
    path('<int:id>/',product_detail, name="product_detail"),
    path('add-to-cart/<int:id>/',add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('remove/<int:id>/',remove_from_cart, name='remove_from_cart'),
    path('update/<int:id>/',update_cart, name='update_cart'),
]

