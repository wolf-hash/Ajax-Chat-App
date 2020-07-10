from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'chatroom/home.html')
