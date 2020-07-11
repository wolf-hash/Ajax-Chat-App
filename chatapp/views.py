from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.

def chathome(request):
    if request.user.is_anonymous:
        return redirect('/login')

    rooms = Room.objects.all()
    return render(request, 'chatapp/chathome.html', {'rooms': rooms})

def createroom(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    Room.objects.create(user=request.user, name='name')
    return HttpResponse('check')

def activeroom(request, room_name):
    if Room.objects.filter(name=room_name).exists():
        messages = Message.objects.filter(name=room_name)
        return render(request, 'chatapp/room.html', {'messages': messages})

    return HttpResponseNotFound(render(request, 'chatapp/notfound.html'))