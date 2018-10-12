from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

class AccountForm(forms.Form):
    location = forms.CharField(label='Location', max_length=100)
    about_me = forms.CharField(label='About Me', widget=forms.Textarea)
