from django.contrib import admin

# Register your models here.

from myapp.models import userdata

class userAdmin(admin.ModelAdmin):
    list_display=('id','NAME','PHONE','POINT')


admin.site.register(userdata, userAdmin)






from myapp.models import QAN

class QANAdmin(admin.ModelAdmin):
    list_display=('id','NAMES','QUESTIONS')


admin.site.register(QAN, QANAdmin)