from django.contrib import admin
from .models import *
# Register your models here.

models_list = [Klijent, Polica, Podruznica]

admin.site.register(models_list)