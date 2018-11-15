from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from galleryapp.forms import GalleryForm
from galleryapp.models import Gallerymodel

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            ShelterCode = request.POST.get('ShelterCode','')
            Organization = request.POST.get('Organization','')
            Designation = request.POST.get('Designation','')
            UserName = request.POST.get('UserName','')
            MajorTasks = request.POST.get('MajorTasks','')
            Tasks = request.POST.get('Tasks','')
            Latitude = request.POST.get('Latitude','')
            Longitude = request.POST.get('Longitude','')
            SubDate = request.POST.get('SubDate','')
            Comments = request.POST.get('Comments','')
            Image1Caption = request.POST.get('Image1Caption','')
            Image2Caption = request.POST.get('Image2Caption','')
            Image3Caption = request.POST.get('Image3Caption','')
            Image4Caption = request.POST.get('Image4Caption','')
            Image5Caption = request.POST.get('Image5Caption','')   
        
            if request.FILES['myfile1']:
                myfile1 = request.FILES['myfile1']
                fs = FileSystemStorage()
                filename1 = fs.save(myfile1.name, myfile1)

            if request.FILES['myfile2']:
                myfile2 = request.FILES['myfile2']
                fs = FileSystemStorage()
                filename2 = fs.save(myfile2.name, myfile2)
                    
            if request.FILES['myfile3']:
                myfile3 = request.FILES['myfile3']
                fs = FileSystemStorage()
                filename3 = fs.save(myfile3.name, myfile3)

            if request.FILES['myfile4']:
                myfile4 = request.FILES['myfile4']
                fs = FileSystemStorage()
                filename4 = fs.save(myfile4.name, myfile4)
            if request.FILES['myfile5']:
                myfile5 = request.FILES['myfile5']
                fs = FileSystemStorage()
                filename5 = fs.save(myfile5.name, myfile5) 
                print(filename5)
    
            gallery_obj = Gallerymodel(ShelterCode=ShelterCode,Organization=Organization,Designation=Designation,UserName=UserName,MajorTasks=MajorTasks,Tasks=Tasks,Latitude=Latitude,Longitude=Longitude,SubDate=SubDate,Comments=Comments,Image1=filename1,Image1Caption=Image1Caption,Image2=filename2,Image2Caption=Image2Caption,Image3=filename3,Image3Caption=Image3Caption,Image4=filename4,Image4Caption=Image4Caption,Image5=filename5,Image5Caption=Image5Caption)
            gallery_obj.save() 
        
    else:
        form = GalleryForm()
    return render(request,'index.html',{
        'form':form,
    })

 




