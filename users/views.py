from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='account_login')
def index(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    else:
        return HttpResponse(f'You are logged in as {request.user.email}, to logout press <a href="logout">Logout</a>')

def logout_view(request):
    logout(request)
    return redirect('/')


def signin(request):
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # next = request.POST.get('next')
    pass


def signup(request):
    pass
