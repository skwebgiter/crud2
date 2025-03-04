from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.name