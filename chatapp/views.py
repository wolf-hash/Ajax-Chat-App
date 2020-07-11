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
    
    clientip = request.META['REMOTE_ADDR']
    room = Room.objects.create(user=request.user, name='test', ipaddress=clientip)
    return HttpResponse('check')

def activeroom(request, room_name):
    if not request.user.is_anonymous:
        if Room.objects.filter(name=room_name).exists():
            messages = Message.objects.filter(name=room_name)
            return render(request, 'chatapp/room.html', {'messages': messages})

        else:
            return HttpResponseNotFound(render(request, 'chatapp/notfound.html'))

    return redirect('/login')