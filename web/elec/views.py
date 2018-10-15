from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import NameForm, AccountForm, RegistrationForm
from .models import AccountInfo
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'home.html')


def loginer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            # redirect to a new URL:

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                form = NameForm()
                return render(request, 'login.html', {'form': form, 'error':'Wrong credentials'})

    # if a GET (or any other method) we'll create a blank form
    else:
        if request.user.is_authenticated:
            return redirect('/profile/')
        else:
            form = NameForm()

    return render(request, 'login.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('/register/')

def register(request):
    if request.user.is_authenticated == True:
        return redirect('/profile/')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = RegistrationForm()

    return render(request, 'register.html', {'form': form})



def accountedit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                user_obj = User.objects.get(username=request.user)
                try:
                     AccountInfo.objects.get(user=user_obj)
                except ObjectDoesNotExist:
                     kek = AccountInfo(user=User.objects.get(username=User.objects.get(username=request.user)), location='Default location', about_me="Default about me")
                     kek.save()

                account_obj = AccountInfo.objects.get(user=user_obj)
                account_obj.location = request.POST['location']
                account_obj.about_me = request.POST['about_me']
                account_obj.save()
        else:
            form = AccountForm()

    else:
        return redirect('/register/')

    return render(request, 'accsettings.html', {'form':form})

def bye(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')

def home(request):
    return render(request, 'home.html')


def thanks(request):
    return HttpResponse("Thanks.")
