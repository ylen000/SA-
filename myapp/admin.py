from django.contrib import admin

# Register your models here.

from myapp.models import userdata

class userAdmin(admin.ModelAdmin):
    list_display=('id','NAME','PHONE','POINT')


admin.site.register(userdata, userAdmin)


#QA問題回報表
from myapp.models import QA
class QAAdmin(admin.ModelAdmin):
    list_display=('id','QUESTIONS','USERNAME')
admin.site.register(QA,QAAdmin)

#PRODUCT
from myapp.models import Product
class productAdmin(admin.ModelAdmin):
    list_display=('id','name','point','quantity','intro','total','date')
admin.site.register(Product,productAdmin)