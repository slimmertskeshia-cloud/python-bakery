from django.db import models
from django.contrib.auth.models import User

class CakeFlavor(models.Model):
    """A flavor like Chocolate, Vanilla, or Red Velvet."""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Topping(models.Model):
    """A topping specific to a cake flavor."""
    cake_flavor = models.ForeignKey(CakeFlavor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name