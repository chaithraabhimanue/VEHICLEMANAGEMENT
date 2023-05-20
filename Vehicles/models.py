from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=200)
    vehicle_number=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    owner=models.CharField(max_length=200)
    km_driven=models.PositiveIntegerField()
    purchased_date=models.DateField(null=True)
    options=(("petrol","petrol"),("diesel","diesel"),("ev","ev"))
    fuel_type=models.CharField(max_length=200,choices=options)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_number
