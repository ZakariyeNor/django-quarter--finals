from django import forms
from .models import CollaborateRequest

#Create your form here
class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')