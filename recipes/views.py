from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home(request):
    return render(request, 'recipes/pages/home.html')

