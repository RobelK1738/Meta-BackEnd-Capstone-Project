from django.db import models

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self):
        return self.Name
    
class MenuItems(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    
    def __str__(self):
        return self.Title
    
class SingleMenuItem(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    