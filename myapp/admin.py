# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Grades, Students


# Register your models here.
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2


class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 10
    #
    # # 添加、修改页属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    fieldsets = [
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]


class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # # 列表页属性
    list_display = ['pk', 'sname', 'sage', gender, 'scontent', 'sgrade', 'isDelete']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 10

    # # 添加、修改页属性
    fields = ['sname', 'sage', 'sgender', 'scontent', 'sgrade', 'isDelete']
    # fieldsets = [
    #     ("num", {"fields": ['ggirlnum', 'gboynum']}),
    #     ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    # ]


admin.site.register(Grades, GradesAdmin)
admin.site.register(Students, StudentsAdmin)
