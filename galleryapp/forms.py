from django import forms
from galleryapp.models import Gallerymodel


class GalleryForm(forms.ModelForm):
    """ 
    ShelterCode = forms.IntegerField()
    Organization = forms.CharField(max_length=255)
    Designation = forms.CharField(max_length=255)
    UserName = forms.CharField(max_length=255)
    MajorTasks = forms.CharField(max_length=255)
    Tasks = forms.CharField(max_length=255)
    Latitude = forms.FloatField()
    Longitude =forms.FloatField()
    SubDate = forms.DateField()
    Comments = forms.CharField(max_length=1000)
    Image1 = forms.CharField(max_length=255)
    Image1Caption = forms.CharField(max_length=255)
    Image2 = forms.CharField(max_length=255)
    Image2Caption = forms.CharField(max_length=255)
    Image3 = forms.CharField(max_length=255)
    Image3Caption = forms.CharField(max_length=255)
    Image4 = forms.CharField(max_length=255)
    Image4Caption = forms.CharField(max_length=255)
    Image5 = forms.CharField(max_length=255)
    Image5Caption = forms.CharField(max_length=255) 
    """
    class Meta:
       model = Gallerymodel
       fields = (
            'ShelterCode',
            'Organization',
            'Designation',
            'UserName',
            'MajorTasks',
            'Tasks',
            'Latitude',
            'Longitude',
            'SubDate',            
            'Comments',            
            'Image1Caption',           
            'Image2Caption',            
            'Image3Caption',            
            'Image4Caption',            
            'Image5Caption',
        )
   