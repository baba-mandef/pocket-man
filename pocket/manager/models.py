from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    name = models.CharField(max_length=150)
    amount = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.IntegerField() #0-> expense 1-> income

class Prevision(models.Model):
    name = models.CharField(max_length=150)