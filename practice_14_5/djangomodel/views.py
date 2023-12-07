from django.shortcuts import render

# Create your views here.

def modelsForm(request):
    return render(request, './djangomodel/models.html')