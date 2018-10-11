from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import NameForm

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


def thanks(request):
    return HttpResponse("Thanks.")
