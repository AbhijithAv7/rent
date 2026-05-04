from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()