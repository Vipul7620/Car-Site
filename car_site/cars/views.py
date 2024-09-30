# cars/views.py

from django.shortcuts import render
from .models import Car  # Assuming you have a Car model
from django.core.files.storage import FileSystemStorage

def car_list(request):
    cars = Car.objects.all()  # Fetching all cars from the database
    return render(request, 'cars/car_list.html', {'cars': cars})

def upload_car(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'cars/car_list.html', {'uploaded_file_url': uploaded_file_url})

    return render(request, 'cars/car_list.html')
