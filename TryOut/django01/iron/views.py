from django.shortcuts import render

# Create your views here.
def app(req):
    return render(req,'iron/index.html')
