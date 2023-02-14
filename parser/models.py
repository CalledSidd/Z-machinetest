from django.db import models

# Create your models here.
class Car(models.Model):
    class Engine(models.IntegerChoices):
        V = 0
        Straight = 1
    class Transmission(models.IntegerChoices):
        Automatic = 0
        Manual = 1
    name = models.CharField(max_length=100)
    miles_per_gallon = models.FloatField(default = 0)
    cylinders = models.IntegerField(default = 0)
    displacement = models.CharField(max_length=20)
    horsepower = models.IntegerField(default = 0)
    drat = models.FloatField()
    weight = models.FloatField()
    quarter_mile = models.FloatField()
    configuration = models.IntegerField(choices = Engine.choices)
    transmission = models.IntegerField(choices = Transmission.choices)
    gears = models.IntegerField()
    carburetors = models.IntegerField()

    def __str__(self):
        return self.name

