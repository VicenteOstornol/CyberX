from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
# Create your views here.




def index(request):
    return render(request, 'cyberXapp/index.html', {
    })

def about(request):
    return render(request, 'state_logged_out/about.html', {
    })

def contact(request):
    return render(request, 'state_logged_out/contact.html', {
    })

def login(request):
    return render(request, 'state_logged_out/login.html', {
    })


