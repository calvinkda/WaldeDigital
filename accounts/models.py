from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=255, null=True)
    adresse = models.TextField(null=True)
