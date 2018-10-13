from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import NameForm, AccountForm
from .models import AccountInfo

def index(request):
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
                return HttpResponseRedirect('/thanks/')
            else:
                return HttpResponse('This is an errorous login attempt')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'base.html', {'form': form, 'user':'Username', 'pass':'Password'})

def register(request):
    if request.user.is_authenticated == True:
        return HttpResponse("You are already logged in.")
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thanks/')
        else:
            form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def accountedit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                if AccountInfo(user=User.objects.get(username=request.user)) == User.objects.get(username=request.user):
                    user_obj = User.objects.get(username=request.user)
                else:
                    kek = AccountInfo(user=User.objects.get(username=User.objects.get(username=request.user)), location='Default location', about_me="Default about me")
                    kek.save()
                    user_obj = User.objects.get(username=request.user)

                account_obj = AccountInfo.objects.get(user=user_obj)
                account_obj.location = request.POST['location']
                account_obj.about_me = request.POST['about_me']
                account_obj.save()
        else:
            form = AccountForm()

    return render(request, 'user.html', {'form':form})

def thanks(request):
    return HttpResponse("Thanks.")
