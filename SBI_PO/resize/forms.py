from django import forms
from models import *
from django.core.validators import RegexValidator

class image_upload_form(forms.ModelForm):
        FirstName = forms.CharField()
	LastName = forms.CharField()
	EmailAddress = forms.EmailField(help_text="Eg.: example@sample.com")
	phone_regex = RegexValidator(regex=r'^[7-9]{1}[0-9]{9}$', message="Phone number must be entered in the format: '9876543210'")
	Phone = forms.CharField(max_length=10, validators=[phone_regex], help_text="Eg.: 9876543210")
        path = forms.ImageField(help_text="Upload Image")
	
	class Meta:
                model = image_upload
                fields = []
