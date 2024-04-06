from django.shortcuts import render
from . models import AboutMe, Testimonies

# Create your views here.

def index(request):
    descriptions = AboutMe.objects.all()
    testimonies = Testimonies.objects.all()
    context = {
        'descrptions': descriptions, 
        'testimonies': testimonies
    }
    return render(request, 'index.html', context)