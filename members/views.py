from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
# import requests
import http.client
import config


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect(reverse('home'))
        else:
            messages.success(request, ("there was an error logging in, try again"))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email)

    else:
        form = UserCreationForm()
    return render(request, 'registration/register_user.html', {
        'form': form
    })


# this gets individual team stats
def select_team(request):

    rapid_api = config.rapid_api_key

    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
    'X-RapidAPI-Key': rapid_api,
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/teams?id=33", headers=headers)

    res = conn.getresponse()

    if res.status == 200:
        print('working')
        data = res.read()
        return render(request, 'registration/select_team.html', {'data': data.decode})
    else:
        print('error')
        return render(request, 'registration/select_team.html', {'error': res.status})