from django.db import models

# Create your models here.
class Car(models.Model):
    license_plate = models.CharField(
        #06KG918IB
        #123456789
        max_length=10,
        verbose_name="Госномер авто"
    )
    brand = models.CharField(
        max_length=200
    )
    model = models.CharField(
        max_length=200
    )
    steering_wheel = models.CharField(
        max_length=20
    )
    color = models.CharField(
        max_length=100
    )
    year = models.CharField(
        max_length=10
    )
    volume = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.license_plate
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"