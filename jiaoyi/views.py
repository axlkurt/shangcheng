#coding:utf-8
from django.shortcuts import render 
from django.http import HttpResponse



def moban(request):
    string = U"第一个变量显示内容。。。"
    kurt = U"第二个变量显示内容"
    return render(request, 'home.html',{'string':string,'kurt':kurt})
