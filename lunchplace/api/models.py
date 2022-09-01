from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Employee'


class Restaurant(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.IntegerField()
    restaurant_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
