import factory
from factory.django import DjangoModelFactory
from main.models import *

class PodruznicaFactory(DjangoModelFactory):
    class Meta:
        model = Podruznica

    mjesto = factory.Faker("city")

class PolicaFactory(DjangoModelFactory):
    class Meta:
        model = Polica
    
    vrsta = factory.Faker("country")
    trajanje = factory.Faker('pyint', min_value=1, max_value=8)


class KlijentFactory(DjangoModelFactory):
    class Meta:
        model = Klijent
    
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    datum_rodenja = factory.Faker("date_time")
    podruznica = factory.Iterator(Podruznica.objects.all())
    polica = factory.Iterator(Polica.objects.all())

