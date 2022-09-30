from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def frontend(request):
    return render(request,'index.html')

def backend(request):
    return render(request,'backend.html')