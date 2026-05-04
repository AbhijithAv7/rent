from django.db import models
from django.contrib.auth import get_user_model
from dresses.models import Dress
User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    days = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)