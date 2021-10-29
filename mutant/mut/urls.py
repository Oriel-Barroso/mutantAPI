from django.urls import path 
from .views import *


urlpatterns = [
    path('tomaradn/', tomarADN),
    path('verificarADN/<int:pk>/', verificarADN)
]