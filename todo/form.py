from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from todo.models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label="ایمیل")
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']           