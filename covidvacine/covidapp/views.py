from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.

def covidreg(request):


    return render(request,"cities.html")

