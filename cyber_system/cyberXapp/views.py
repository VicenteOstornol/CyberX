from django.shortcuts import render, redirect
from django.views import generic
from . import models
from .forms import ComputerForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

def index_in(request):
    return render(request, 'state_logged_in/index_in.html', {
    })


def computer_management(request):
    computers = models.Computer.objects.all()

    return render(request, 'state_logged_in/computers_detail.html',
    {'computers': computers})

def computer_detail(request, pk):
    computer = models.Computer.objects.get(id=pk)
    return render(request, 'state_logged_in/computer_detail.html', 
    {'computer': computer})


def computer_edit(request, pk):
    computer = models.Computer.objects.get(id=pk)
    form = ComputerForm(instance=computer)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('computer_management')
    return render(request, 'state_logged_in/add_editComputer.html', 
    {'form_':form})

def computer_delete(request, pk):
    computer = models.Computer.objects.get(id=pk)
    if request.method == 'POST':
        computer.delete()
        return redirect('computer_management')
    return render(request, 'state_logged_in/computer_delete.html', 
    {'computer': computer})

def add_editComputer(request):
    form = ComputerForm()
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computer_management')
    return render(request, 'state_logged_in/add_editComputer.html', 
    {'form_':form})