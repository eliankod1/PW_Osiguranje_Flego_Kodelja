from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factory import *

NUM = 10

class Command(BaseCommand):
    help = "This command generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Deleting old data...")
        models = [Podruznica, Klijent, Polica]
        for model in models:
            model.objects.all().delete()

        self.stdout.write("Creating new data...")
        for i in range(NUM):
            PodruznicaFactory()

        for i in range(NUM):
            PolicaFactory()

        for i in range(NUM):
            KlijentFactory()
