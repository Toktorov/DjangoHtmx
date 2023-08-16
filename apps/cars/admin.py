from django.contrib import admin

from apps.cars.models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'brand', 'model', 'year')