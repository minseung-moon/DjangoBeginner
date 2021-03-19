from django.contrib import admin
from .models import Board
# Register your models here.


# 관리자에서 사용할 정보를 기입


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Board, BoardAdmin)
