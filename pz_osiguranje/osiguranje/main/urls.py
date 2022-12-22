from django.urls import path, include
from . import views
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('podruznica/', PodruznicaList.as_view()),
    path('klijent/', KlijentList.as_view()),
    path('polica/', PolicaList.as_view()),
]
