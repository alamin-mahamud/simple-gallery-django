from django.shortcuts import render
from galleryapp.models import Gallerymodel


# Create your views here.
def show(request):
    gallerymodel = Gallerymodel.objects.all()
    return render(request, 'galleryshow.html', {'gallerymodel': gallerymodel}) 

def display(request):
    gallerymodel1 = Gallerymodel.objects.all()
    return render(request, 'display.html', {'gallerymodel1': gallerymodel1}) 