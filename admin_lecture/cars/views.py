from django.shortcuts import render
from . import models

# Create your views here.
def list(request):
  all_cars = models.Car.objects.all()
  context = { "all_cars": all_cars }

  return render(request, 'cars/list.html', context = context)

def add(request):
  return render(request, 'cars/add.html')

def delete(request):
  return render(request, 'cars/delete.html')

