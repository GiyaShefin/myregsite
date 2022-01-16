from django.shortcuts import render

# Create your views here.

def detail_patient(request):
    return render(request, 'vaccinationbooking.html')

def success_page(request):
    return render(request, 'success.html')

