from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class NameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class AccountForm(forms.Form):
    location = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    about_me = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control'}))
    #first_name = forms.CharField(label='First Name', widget=forms.Textarea(attrs={'class':'form-control'}))
    #last_name = forms.CharField(label='last Name', widget=forms.Textarea(attrs={'class':'form-control'}))
    #email_address = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class':'form-control'}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password1 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class ChangeMeForm(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))

class AddPostsForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class':'form-control'}))
    post = forms.CharField(label='Post', widget=forms.Textarea(attrs={'class':'form-control'}))

class NewsForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control'}))
    post = forms.CharField(label='Post', widget=forms.Textarea(attrs={'class':'form-control'}))
