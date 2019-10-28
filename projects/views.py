# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import RegisterForm
from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('projects:welcome')
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

