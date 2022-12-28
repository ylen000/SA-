from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.   

def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
# Create your views here.
