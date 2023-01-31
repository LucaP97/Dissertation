from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.success(request, ("there was an error logging in, try again"))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
