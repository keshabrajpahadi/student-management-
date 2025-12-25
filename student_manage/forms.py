from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={
            "fname":"First Name",
            "lname":"Last Name",
            "email":"Email",
            "phone":"Phone Number",
        }
        widgets={
            "fname":forms.TextInput(attrs={"class":"form-control"}),
            "lname":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "branch":forms.Select(attrs={"class":"form-control"})
        }

'''
class SignupForm(UserCreationForm):
    password1=forms.CharField(label='password',
    widget=forms.PasswordInput(attrs={'class':'form-contrl'}))
    password2=forms.CharField(label='confirm password',
    widget=forms.PasswordInput(attrs={'class':'form-contrl'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'first_name','last_name':'last_name','email':'email'}
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.EmailInput(attrs={"class":"form-control"}),
            "email":forms.NumberInput(attrs={"class":"form-control"})
        } '''