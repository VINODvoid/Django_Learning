from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app(req):
    return render(req,'iron/index.html')

def order(req):
    return render(req,'iron/order.html')
    