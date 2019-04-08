from django.db import models


class Product(models.Model):
    name = models.ForeignKey(to='Vegetable', on_delete=models.CASCADE)
    price = models.FloatField()
    unit = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.name


class Vegetable(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
