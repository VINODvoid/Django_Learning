from django.shortcuts import render
from .models import *
# Create your views here.
def recipes(req):
    if req.method == 'POST':
        data = req.POST
        if 'image' in req.FILES:
            image = req.FILES['image']
            name = data.get('name')
            description = data.get('description')
            print(name)
            print(description)
            print(image)
            Recipe.objects.create(
                name=name,
                description=description,
                image=image
            )
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(req,'index.html',context)
    
def collection(req):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(req,'collection.html',context)