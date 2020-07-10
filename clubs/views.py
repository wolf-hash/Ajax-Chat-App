from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'clubs/index.html')

def events(request):
    return render(request, 'clubs/events.html')

def recruitments(request):
    return render(request, 'clubs/recruitments.html')


            
