from django.shortcuts import render

# Create your views here.
def recipes(req):
    data = req.POST
    print(data)
    return render(req, 'recipes.html')
    