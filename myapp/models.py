from django.db import models

# Create your models here.
class userdata(models.Model):

        NAME = models.CharField('使用者名稱',max_length=20, null=False)
        PHONE = models.CharField('手機',max_length=10, null=False)
        PASSWORD = models.CharField('密碼',max_length=20, null=False)
        NICKNAME = models.CharField('暱稱',max_length=20,blank=True)
        POINT = models.IntegerField('點數',blank=True)
        IDCARD = models.CharField('身分證字號',max_length=10,blank=True)



class QAN(models.Model):
        NAMES = models.CharField('使用者名稱',max_length=20, null=False)
        QUESTIONS = models.CharField('問題回報',max_length=500,blank = False,null=False)
        

#class memberlevel(models.Model):
       # IMAGE = models.ImageField(upload_to="../static/images",blank=False, null=False)
        #IMAGE_NUMBER = models.CharField('等級',max_length=32)
