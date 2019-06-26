from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")

def register(request):

    return render(request,'blog.html')

def send(request):

    email =request.POST('Email1')
    password = request.POST('Password1')
    context={'email':email,'password':password}
    return render(request,'successful.html',context)

