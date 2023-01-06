from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import userdata
from myapp.models import Product
from myapp.models import QA
from django.http import Http404
from django.contrib import auth
from django.db.models import F, Func, Value
from django.db.models import Max
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from myapp.models import userbuy
from datetime import date
from django.urls import path
#from myapp import flask_app

# Create your views here.
#urlpatterns=[
# path('/flask',flask_app.home)
# ]
def signin(request):
    username=request.session.get('username')
    if username is not None:
        user=userdata.objects.get(NAME=username)
        name=str(user.NAME)
        return render(request, 'usersignin.html',locals())
    else:
        return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
def register(request):
    uName =request.POST.get('username')
    uPhone =request.POST.get('phone')
    uPassword =request.POST.get('password')
    if uName =="":
        wrong="有欄位空白"
        a="http://127.0.0.1:8000/register"
        back="註冊頁面"
        return render(request,'QAsuccess.html',locals())
    if uPhone =="":
        wrong="有欄位空白"
        a="http://127.0.0.1:8000/register"
        back="註冊頁面"
        return render(request,'QAsuccess.html',locals())
    if uPassword =="":
        wrong="有欄位空白"
        a="http://127.0.0.1:8000/register"
        back="註冊頁面"
        return render(request,'QAsuccess.html',locals())
    else:
        rg = userdata(NAME=uName,PHONE=uPhone,PASSWORD=uPassword)
        rg.save()
        return render(request, 'signin.html',locals())
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
def signout(request):
    request.session.clear()
    return render(request, 'signin.html')
def home(request):
    username=request.session.get('username')
    return render(request,'index.html',locals())
def rank(request):
    username=request.session.get('username')
    ranking_list=userdata.objects.all().order_by('-POINT')
    rank = ranking_list.filter(POINT__gt=ranking_list.get(NAME=username).POINT).count() + 1
    return render(request,'leaderboard.html',locals())

def product(request):
    return render(request, 'product_01.html')


#def rerank(request):
def point(request):
    return render(request, 'pointsmall.html')
           


def QAQ (request):
    return render(request, 'QA.html')
def QAw(request):
    q = request.POST.get('question')
    if q =="":
        wrong="未填入任何有效字符"
        a="http://127.0.0.1:8000/123"
        back="問題回報"
        return render(request,'QAsuccess.html',locals())
    else:
        username=request.session.get('username')
        problem = QA(USERNAME=username,QUESTIONS=q)
        problem.save()
        wrong="回報成功，感謝您的寶貴意見"
        a="http://127.0.0.1:8000/login/index"
        back="首頁"
        return render(request,'QAsuccess.html',locals())
    
    
# Create your views here.
def member(request):
          username=request.session.get('username')
          user=userdata.objects.get(NAME=username)
          img=str(user.user_image)
          userphone=str(user.PHONE)
          name=str(user.NAME)
          name=str(user.NAME)


          #user = User.objects.get(username='username')
          #mypoint= str(request.GET.get('POINT'))
          #mylevel= str(request.GET.get('IMAGE_NUMBER'))
          point=str(user.POINT)
          point1=int(user.POINT)
          if point1>=15000:
            levels=1
          elif 14999<=point1<9000:
            levels=2
          elif 8999<=point1<6000:
            levels=3
          elif 5999<=point1<3000:
            levels=4
          elif 2999<=point1<1000:
            levels=5
          else:
            levels=6
         
          return render(request,'member.html',locals())

def receip(request):
    username=request.session.get('username')
    user=userdata.objects.get(NAME=username)
    name=str(user.NAME)
    point=str(user.POINT)
    img=str(user.user_image)
    return render(request,'receip.html',locals())



def product(request):
    nname=Product.objects.get(id=2)
    return render(request, 'product_01.html',locals())

def change(request):
    username=request.session.get('username')
    num=request.GET.get('num')
    proname=str(request.GET.get('product'))
    product=Product.objects.get(name=proname)
    Point=product.point
    total=int(num)*Point
    return render(request, 'change.html',locals())

def reducepoint(request):
    username=request.session.get('username')
    userpoint=userdata.objects.get(NAME=username)
    total=request.GET.get('total')
    product=request.GET.get('product')
    l=int(userpoint.POINT)-int(total)
    userpoint.POINT=l
    userpoint.save()
    record = userbuy(USERNAME=username,PNAME=product,EX=total,LEFT=l,DATE=date.today())
    record.save()
    return render(request, 'buysuccess.html',locals())
def grade(request):
    return render(request, 'grade.html')
def memberlook(request):
    username=request.session.get('username')
    try:
        userbuys = userbuy.objects.filter(USERNAME=username)
    except userbuy.DoesNotExist:
        raise Http404("查無資料")
    except:
        raise Http404("讀取錯誤")
    return render(request, 'memberlook1.html',locals())
    
def add(request):
    # =====新增的程式碼=====#
    username=request.session.get('username')
    user=userdata.objects.get(NAME=username)
    img=str(user.user_image)
    userphone=str(user.PHONE)
    name=str(user.NAME)
    point1=int(user.POINT)
    levels=1
    if point1>=1000000:
        levels=0
    elif 15000<=point1<1000000:
        levels=1
    else:
        level="--"
    if request.method == "POST":
        user_img = request.FILES.get('user_image')
        phone = request.POST.get('phone')
        aname = request.POST.get('myname')
        user=userdata.objects.get(NAME=username)
        user.user_image = user_img
        user.save()
        img=user.user_image
    return render(request, 'member.html', locals())
def res(request):
    return render(request,'memberedit.html')
def re(request):
    # =====新增的程式碼=====#
        username=request.session.get('username')
        user=userdata.objects.get(NAME=username)
        img=str(user.user_image)
        userphone=str(user.PHONE)
        name=str(user.NAME)
        point1=int(user.POINT)
        levels=1
        if point1>=1000000:
            levels=0
        elif 15000<=point1<1000000:
            levels=1
        else:
            level="--"
        if request.method == "POST":
            phone = request.POST.get('phone')
            aname = request.POST.get('myname')
            user=userdata.objects.get(NAME=username)
            user.NAME = aname
            user.PHONE=phone
            user.save()
        return render(request, 'member.html', locals())


