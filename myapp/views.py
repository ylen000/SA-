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
    uPass = request.POST.get('psw')
    try:
        user=userdata.objects.get(PHONE=uName)

        if uPass==user.PASSWORD:
                #userlogin = request.session.get(uName)
            username=str(user.NAME)
            request.session["username"]=username
            return render(request, 'welcome.html',locals())
        else:
            wrong="帳號或密碼錯誤!!"
            return render(request,'passwordwrong.html',locals())
    except userdata.DoesNotExist:
            wrong="尚未註冊"
            return render(request,'passwordwrong.html',locals())

def home(request):
    username=request.session.get('username')
    return render(request,'index.html',locals())
def member(request):
         # membername==request.session.get('username')
          username=request.session.get('username')
          user=userdata.objects.get(NAME=username)
          userphone=str(user.PHONE)


          #user = User.objects.get(username='username')
          #mypoint= str(request.GET.get('POINT'))
          #mylevel= str(request.GET.get('IMAGE_NUMBER'))
          return render(request,'member.html',locals())





# Create your views here.
