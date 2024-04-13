from django.shortcuts import render
from . models import AboutMe, Testimonies
from . models import Blog

# Create your views here.

def index(request):
    descriptions = AboutMe.objects.all()
    testimonies = Testimonies.objects.all()
    articles = Blog.objects.all()
    context = {
        'descrptions': descriptions, 
        'testimonies': testimonies,
        'articles': articles,
    }
    return render(request, 'index.html', context)