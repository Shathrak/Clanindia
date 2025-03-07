# example/views.py
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
#   return render(request, 'Home.html' )///

def login(request):
    return render(request, 'Login.html')

def g_choice(request):
    return render(request, 'game_choice.html')

def match(request):
    return render(request, 'match.html')

def profile(request):
    return render(request, 'profile.html')