from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'Place {self.name} | {self.address}'

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizzas = models.BooleanField(default=False)


    def __str__(self):
        return f'Restraurant {self.name} | {self.address}'