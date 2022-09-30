from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_in/', views.index_in, name='index_in'),
    # path('create/customer/', views.create_customer(), name='costumer'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('computer_management/', views.computer_management, name='computer_management'),
    path('add_edit_computer/', views.add_editComputer, name='add_editComputer'),
    path('computer_detail/<int:pk>/', views.computer_detail, name='computer_detail'),
    path('computer_edit/<int:pk>/', views.computer_edit, name='computer_edit'),
    path('computer_delete/<int:pk>/', views.computer_delete, name='computer_delete'),
]