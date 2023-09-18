from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout


def index(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    else:
        return HttpResponse(f'You are logged in as {request.user.email}, to logout press <a href="logout">Logout</a>')

def logout_view(request):
    logout(request)
    return redirect('/')
