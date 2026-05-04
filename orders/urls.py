from django.urls import path
from .views import *


urlpatterns = [
    path('payment/',payment_page, name="payment"),
]
