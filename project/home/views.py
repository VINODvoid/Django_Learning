from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(req):
    people = [{
        "name":"abhi",
        "age":10
    },
    {
        "name":"abhishek",
        "age":21
    },
    {
        "name":"rahul",
        "age":32
    }]
    title = {'title':"Home Page"}
    vegetables =['Tomato','Onion','Potato','Garlic','Ginger' ]
    return render(req,'index.html',context={"people":people,'vegetables':vegetables,'title':title})

def about(req):
    title = {'title':"About"}
    return render(req, 'about.html',context=title)

def contact(req):
    title={'title':"Contact"}
    return render(req, 'contact.html',context=title)
