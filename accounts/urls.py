from django.urls import path
from .views import*

urlpatterns = [
    path('register/',register, name="register"),
    path('login/',user_login, name="login"),
    path('logout/',user_logout, name="logout"),
    path('profile/',profile_view, name='profile'),
    path('dashboard/',admin_dashboard, name='admin_dashboard'),
    path('add-category/', add_category, name='add_category'),
    path('add-product/', add_product, name='add_product'),
    path('orders/', view_orders, name='view_orders'),
    path('users/', view_users, name='view_users'),
]
