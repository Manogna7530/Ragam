from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from Accounts.decorators import unauthenticated_user
from Accounts.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
from Accounts.decorators import *
import pandas as pd
from django.conf import settings
from django.contrib.auth.models import Group
from django.views.decorators.cache import never_cache


from django.apps import apps

models = {
    model.__name__: model for model in apps.get_models()
}

User = get_user_model()
# Create your views here.
@never_cache
@unauthenticated_user
def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            userId = user.id
            unVerifiedUser = User.objects.get(id=userId) 
            auth.login(request, user)
            return redirect('Accounts:home', permanent=True)
        
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('Accounts:login', permanent=True)
    else:
        form = LoginForm()
        return render(request, 'Accounts/login.html', {'title': 'Login', 'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request,'Logged Out Successfully!')
    return redirect('/')



        
       
        
   


@never_cache
@login_required(login_url='Accounts:login')
@group_review
@allowed_users(allowed_roles=['admin'])
def home(request):
    context = { 'title': 'Ganam | Home'}
    return render(request, 'Accounts/home.html',context)

