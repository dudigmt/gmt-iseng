from django.db import models

class Employee(models.Model):
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=20, unique=True)
    departemen = models.CharField(max_length=50)
    posisi = models.CharField(max_length=50)
    tgl_masuk = models.DateField()
    gaji = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nama} - {self.nik}"