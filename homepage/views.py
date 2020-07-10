from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def index(request):
    return render(request, 'homepage/index.html')

def Login(request):
    if request.method == 'POST':
        regno = request.POST.get('regno')
        password = request.POST.get('password')
        user = authenticate(username=regno, password=password)
        if user is not None:
            login(request, user)
            return redirect('/chatroom')
        else:
            return redirect('/login')
        
    return render(request, 'homepage/login.html')

def Logout(request):
    logout(request)
    return redirect('/login')

def Signup(request):
    if request.method == 'POST':
        regno = request.POST.get('regno')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.create_user(username=regno, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('/login')
    return render(request, 'homepage/signup.html')