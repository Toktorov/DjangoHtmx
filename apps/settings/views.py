from django.shortcuts import render
from django.http import JsonResponse

from apps.cars.models import Car

# Create your views here.
def index(request):
    if request.method == "POST":
        license_plate = request.POST.get('license_plate').upper()
        try:
            car = Car.objects.get(license_plate=license_plate)
            context = {'car' : car}
            return render(request, 'index.html', context)
        except:
            return render(request, 'index.html')
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())