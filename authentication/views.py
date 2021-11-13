from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == 'secure_password':
                response = redirect('/dashboard/')
                response.set_cookie('password', True)
                return response
    else:
        form = CreateAccountForm()

    context = {
        'form': form
    }
    return render(request, 'authentication/login.html', context)


