from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserRegisterationForm, UserLoginForm
from Inventory.models import Transaction, Client, Item



def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterationForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=username, password=password)
        login(request,new_user)

        if next:
            return redirect(next)
        return redirect('Inventory:index')

    return render(request,'accounts/registeration.html', {'form':form})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)

        return redirect('Inventory:index')

    return render(request, "accounts/login.html" ,{'form':form})



def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def profile_view(request):
    transaction = Transaction.objects.all()
    return render(request, 'accounts/profile-view.html', {'transaction':transaction})