from django.contrib import admin
from .models import Board
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)  # 리스트엔 타이틀만 나오게


admin.site.register(Board, BoardAdmin)  # 보드 어드민 연결
