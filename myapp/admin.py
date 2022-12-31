from django.contrib import admin

# Register your models here.

from myapp.models import userdata

class userAdmin(admin.ModelAdmin):
    list_display=('id','NAME','PHONE','POINT')
admin.site.register(userdata, userAdmin)


from myapp.models import QA
class QAAdmin(admin.ModelAdmin):
    list_display=('USERNAME','QUESTIONS')
admin.site.register(QA, QAAdmin)