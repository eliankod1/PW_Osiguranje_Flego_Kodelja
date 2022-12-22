from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from main.models import *
# Create your views here.

def homepage(request):
    return render(request, "index.html")

class PodruznicaList(ListView):
    model = Podruznica

class KlijentList(ListView):
    model = Klijent

class PolicaList(ListView):
    model = Polica

