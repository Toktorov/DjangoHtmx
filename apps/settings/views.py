from django.shortcuts import render

from apps.cars.models import Car

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())