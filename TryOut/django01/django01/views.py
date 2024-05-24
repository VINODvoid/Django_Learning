from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest):
    # return HttpResponse("Hello World , Welcome to Django")
    return render(request,'website/index.html')

def about(request: HttpRequest):
    return HttpResponse("Hello World , Welcome to Django,About")

def contact(request: HttpRequest):
    return HttpResponse("Hello World , Welcome to Django,Contact")