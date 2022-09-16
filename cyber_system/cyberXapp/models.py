from django.db import models

# Create your models here.
# this app is for a cyber cafe management system

class Customer(models.Model):
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE)
    rut = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return self.name



class Computer(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    computer_type = models.CharField(max_length=100)
    modal_No = models.CharField(max_length=100)
    computer_series = models.CharField(max_length=100)
    computer_ram = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


