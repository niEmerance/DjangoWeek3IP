from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile,Comment

class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=["prj_title","prj_image","prj_desc","prj_link","user"]

class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['bio'].widget=forms.TextInput()
   class Meta:
       model=Profile
       exclude=['username','likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','prj_comment']