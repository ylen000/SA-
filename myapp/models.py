from django.db import models

# Create your models here.
class userdata(models.Model):

        NAME = models.CharField('使用者名稱',max_length=20, null=False)
        PHONE = models.CharField('手機',max_length=10, null=False)
        PASSWORD = models.CharField('密碼',max_length=20, null=False)
        NICKNAME = models.CharField('暱稱',max_length=20,blank=True)
        POINT = models.IntegerField('點數',blank=True,default=0)
        IDCARD = models.CharField('身分證字號',max_length=10,blank=True)
        



class QA(models.Model):
        USERNAME=models.CharField('使用者名稱',max_length=20,blank=True )
        QUESTIONS = models.CharField('問題回報',max_length=500,blank=True)
class memberlevel(models.Model):
        IMAGE = models.ImageField(upload_to="../static/images",blank=False, null=False)
        IMAGE_NUMBER = models.CharField('等級',max_length=32)



#import datetime
#now = datetime.datetime.now()
# 創建一個Product的實例，並將當時的日期存入 date 字段


from django.db import models
from django.utils import timezone
class Product(models.Model):
        
    name = models.CharField(max_length=255)
    point = models.IntegerField(max_length=500)
    quantity = models.PositiveIntegerField()
    intro = models.CharField(max_length=600)
    total = models.CharField(max_length=20, null=False)
    date = models.DateTimeField(default = timezone.now)

class userbuy(models.Model):
     DATE = models.DateTimeField('日期',default = timezone.now)
     USERNAME=models.CharField('使用者名稱',max_length=20,blank=True )
     PNAME=models.CharField('商品名稱',max_length=255)
     REVENUE=models.CharField('收入',max_length=255)
     EX=models.CharField('支出',max_length=255)
     LEFT=models.CharField('剩餘點數',max_length=255)



