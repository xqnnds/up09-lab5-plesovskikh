from django import forms 
from . import models 

class CreateCommunitie(forms.ModelForm): 
    class Meta: 
        model = models.Community
        fields = ['name','description','slug', 'free','banner']