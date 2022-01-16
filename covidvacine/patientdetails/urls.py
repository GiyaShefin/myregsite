from django.urls import path
from . import views

app_name = "patientdetails"


urlpatterns = [

path('', views.cities, name='cities'),
    path('towns/', views.towns, name='towns'),
]