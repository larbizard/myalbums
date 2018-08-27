# -*- coding: utf-8 -*- 

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm

from django.contrib import messages

def login_view(request):
    next=request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", {"form":form, "title": title})

def register_view(request):
    next=request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        human = True
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_active = False
        user.save()
        new_user = authenticate(username=user.username, password=password)
        # login(request, new_user)
        messages.success(request, "Vous êtes enregistré avec succés. L'administrateur vous avisera lorsque votre compte sera validé.")
        if next:
            return redirect(next)        
        return redirect("/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")