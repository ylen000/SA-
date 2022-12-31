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
         
    
    
            


def QA (request):
    return render(request, 'QA.html')
# Create your views here.
def member(request):
          username=request.session.get('username')
          user=userdata.objects.get(NAME=username)
          userphone=str(user.PHONE)
          name=str(user.NAME)
          name=str(user.NAME)


          #user = User.objects.get(username='username')
          #mypoint= str(request.GET.get('POINT'))
          #mylevel= str(request.GET.get('IMAGE_NUMBER'))
          point=str(user.POINT)
          point1=int(user.POINT)
          if 10000000<=point1:
              level=0
          elif 15000<=point1<1000000:
              level=1
          return render(request,'member.html',locals())

def receip(request):
    username=request.session.get('username')
    user=userdata.objects.get(NAME=username)
    name=str(user.NAME)
    point=str(user.POINT)
    return render(request,'receip.html',locals())







# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import QAN
from django.http import Http404
from django.contrib import auth
def QA(request):
    if request.method == 'GET':
        return render(request, 'QA.html')
    elif request.method == 'POST':
        TXT= request.POST.get('TXT') # login.html 傳來的變數
        #uPass = request.POST.get('uPass') # login.html 傳來的變數
        # 直接判斷帳密有效性
        # if uName=='Peter' and uPass=='591026':
        #     return HttpResponse("已登入")
        # else:
        #     return redirect('/login/')
        
        # 以 Django 內建的管理者帳密判斷有效性
       # user = auth.authenticate(username=uName, password=uPass)
        #if user is not None:
           # auth.login(request, user)
           # return HttpResponse("已登入")
       # else:
           # return redirect('/login/')