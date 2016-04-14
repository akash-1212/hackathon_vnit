from django import forms
from .models import Assignment

class PostForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ('name','course','deadline','file')
