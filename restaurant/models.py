from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length = 255)
    No_of_guests = models.IntegerField(default = 1)
    BookingDate = models.DateTimeField(default = timezone.now)
    
class Menu(models.Model):
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10,decimal_places=2)
    Inventory = models.IntegerField(default = 1)
    
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
    