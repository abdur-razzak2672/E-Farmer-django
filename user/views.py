from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
        
    else:
        form = UserCreationForm()

    if request.user.is_authenticated:
        return redirect('homepage')       
    context = {'form':form}
    return render(request, 'authenticate/register.html', context)


def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            messages.success(request, ("Invalid user name & password"))

            return redirect('login')
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        return render(request,'authenticate/login.html', {})   

@login_required

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('homepage')
