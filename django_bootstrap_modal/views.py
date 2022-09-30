from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def frontend(request):
    return render(request,'index.html')

def backend(request):
    return render(request,'backend.html')

def login(request):
    if request.user.is_authenticated:
        return render(request, "backend.html")
    else:
        messages.info(request, "Please login first to access the page")
        return HttpResponseRedirect('/')