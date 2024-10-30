from django.db import models
from django.urls import reverse
# Create your models here.


class Cars_new(models.Model):
    name_car=models.CharField(max_length=150)
    motor_car=models.CharField(max_length=200)
    firma_car=models.CharField(max_length=200)
    image_car=models.ImageField(upload_to="images/", null=True, blank=True)
    price=models.IntegerField()
    def __str__(self):
        return self.name_car
    def get_absolute_url(self):
        return reverse("newcar", args=[str(self.pk)])

class User(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    phone=models.CharField(max_length=13)
    def __str__(self):
        return self.name
