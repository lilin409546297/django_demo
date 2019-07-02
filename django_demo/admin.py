# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_demo.models import *
# Register your models here.


class RoleInline(admin.TabularInline):
    # 管理员操作关联
    model = Role
    #数量
    extra = 1


# 手动注册/装饰器也可以
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 管理员展示
    list_display = ["id", "name", "age"]
    # 过滤
    list_filter = ["name"]
    # 搜索字段
    search_fields = ["name", "age"]
    # 分页长度
    list_per_page = 10
    # 添加设置
    fieldsets = [
        ("base", {"fields": ["name", "age"]}),
    ]
    # 同时可以操作
    inlines = [RoleInline]


# admin.site.register(User, UserAdmin)
admin.site.register(Role)

