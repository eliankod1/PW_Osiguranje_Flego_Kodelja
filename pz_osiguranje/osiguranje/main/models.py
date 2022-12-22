from django.db import models

# Create your models here.
class Podruznica(models.Model):
    mjesto = models.CharField(max_length=20)

    def __str__(self):
        return self.mjesto

class Polica(models.Model):
    vrsta = models.CharField(max_length=50)
    trajanje = models.IntegerField()

    def __str__(self):
        return self.vrsta

class Klijent(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    datum_rodenja = models.DateField()
    polica = models.OneToOneField(Polica, on_delete=models.CASCADE, blank=True, null=True)
    podruznica = models.ForeignKey(Podruznica, on_delete=models.CASCADE)


    def __str__(self):
        return self.ime

