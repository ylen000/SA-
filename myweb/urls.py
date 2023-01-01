"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin),
    path('signup',views.signup),
    path('login/',views.login),
    path('member/',views.member),
    #path('hi/<username>/', views.hiname),      # 傳遞字串參數 username
    path('login/index',views.home),
    path('login/signin', views.signin),
<<<<<<< HEAD
    path('123',views.QAQ),
    path('QAW/',views.QAw),
<<<<<<< HEAD
    path('login/QA', views.QA),
    path('rank',views.rank)
=======
    path('rank',views.rank),
    path('receip/',views.receip),
=======
    path('receip/',views.receip),
    path('QA/',views.QA, name='greet'),
    path('rank',views.rank),


>>>>>>> bccc6d3043d80f3cb8ff73e1cc4c75ace63da0f4
>>>>>>> 7a9ae47cea0ca7606f4922d6cfd5cba2df7eebc1


    #path('hi/<username>/', views.hinampath('myweb/', include('myweb.urls'))e),      # 傳遞字串參數 username
    #path('age/<int:year>/', views.age),        # 傳遞數值參數 year
    #path('hello/', views.hello_view),
    # path(r'^admin/', admin.site.urls),
    # path(r'^$', sayhello),
]
