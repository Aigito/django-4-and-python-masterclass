from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
  fieldsets = [
    ('MANUFACTURE INFORMATION', {'fields': ["year"]}),
    ('CAR SPECS', {'fields': ["brand"]})
  ]

admin.site.register(Car, CarAdmin)