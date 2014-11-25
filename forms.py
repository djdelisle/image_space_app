from image_space_app.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.core.files.images import get_image_dimensions

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
		
class ImageForm(forms.Form): 
	image = forms.FileField()
