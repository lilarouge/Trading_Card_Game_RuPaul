from django.shortcuts import render, redirect
from .models import Profile
from trading_outpost.models import My_Card, Queens
from django import forms
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required

def my_cards(request):
    if request.method =='GET':
        my_queens= My_Card.objects.all()
        return render(request, 'my_cards.html', {'my_queens': my_queens})

    if request.method=='POST':
        data=request.POST
        print(data)
        card_to_update= My_Card.objects.get(id= data['id'])
        card_to_update.status=data['status']
        card_to_update.save()
    
    
        return redirect('transaction')

def signup(request):

    if request.user.is_superuser:
        messages.error(request, 'You are already signed up and logged in!!')
        return redirect('login')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            # user_profile=User.objects.get(id= user_id)
            # return redirect('profile.html', {'user_profile': user_profile})
            return redirect('profile')

        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/signup.html', {'signupform':form})

def logout(request):
    auth.logout(request)
    return render(request, 'registration/login.html')