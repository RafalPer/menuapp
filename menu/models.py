from django.db import models


class MenuCart(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=500)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.TimeField()
    created_at = models.DateField()
    updated_at = models.DateField()
    is_vegetarian = models.BooleanField()
    menu = models.ForeignKey(MenuCart, on_delete=models.CASCADE, related_name='dish')

    def __str__(self):
        return self.name
