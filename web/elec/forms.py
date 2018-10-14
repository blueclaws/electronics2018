from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class AccountForm(forms.Form):
    location = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    about_me = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control'}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password1 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
