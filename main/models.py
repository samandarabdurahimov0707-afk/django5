from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.pk}. Name: {self.name}"


class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.pk}. Name: {self.name}"
