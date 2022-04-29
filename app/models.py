from tkinter import CASCADE
from django.db import models

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=3, decimal_places=0,null=True, blank=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def total(self):
        total = self.cantidad * self.precio
        return total
