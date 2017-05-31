from django import forms
from models import *

class FilesForm(forms.ModelForm):
    file_path_one = forms.FileField()

    class Meta:
        model = Files
        fields = ["file_path_one"]

