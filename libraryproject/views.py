from django.http import HttpResponse
from django.shortcuts import render
import templates

def home(request):
    return render(request, 'home.html')
