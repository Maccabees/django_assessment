from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse

def home(request):
    request = requests.get('https://openweather.org/')
    return render(request, 'fetchapi/home.html')

def about(request):
    return HttpResponse('<h1> About </h1>')
