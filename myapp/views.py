from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import userdata
from django.http import Http404
from django.contrib import auth

# Create your views here.   

def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
def login(request):
     uName = request.POST.get('uName') 
     uPass = request.POST.get('uPass') 
     user=userdata.objects.filter(PHONE=uName, PASSWORD=uPass)
     if user is not None:
            
            return redirect("您好")
     else:
            return redirect('/login/')

    
# Create your views here.

        