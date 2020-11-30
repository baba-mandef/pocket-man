from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    name = models.CharField(max_length=150)
    amount = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_spent = models.BooleanField()
    is_gain = models.BooleanField()
