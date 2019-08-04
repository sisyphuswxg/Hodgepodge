# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades, Students


# Create your views here.
def index(request):
    return HttpResponse("wangxg loves fifi.")


def detail(request, num1, num2):
    return HttpResponse("detail-%s-%s" % (num1, num2))


def grades(request):
    # 去模板里取数据
    grades_list = Grades.objects.all()
    # 将数据传递给模板，模板再渲染给页面，将渲染的页面返回给浏览器
    return render(request, 'myapp/grades.html', {"grades": grades_list})


def students(request):
    # 去模板里取数据
    students_list = Students.objects.all()
    # 将数据传递给模板，模板再渲染给页面，将渲染的页面返回给浏览器
    return render(request, 'myapp/students.html', {"students": students_list})


def students_in_grade(request, gid):
    grade = Grades.objects.get(pk=gid)
    students_list = grade.students_set.all()
    return render(request, 'myapp/students.html', {"students": students_list})
