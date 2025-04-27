from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Patient(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  age = models.IntegerField(validators = [MinLengthValidator(0), MaxLengthValidator(120)])
  heartrate = models.IntegerField(default = 60, validators = [MinLengthValidator(1), MaxLengthValidator(300)])

  def __str__(self):
     return f"{self.first_name.capitalize()} {self.last_name.capitalize()} is {self.age} years old"