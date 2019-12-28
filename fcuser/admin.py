from django.contrib import admin
from .models import Fcuser

# Register your models here.
# 관리자가 쓸 정보들을 기입


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Fcuser, FcuserAdmin)
