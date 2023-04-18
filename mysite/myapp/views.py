from django.http import HttpResponse
from django.shortcuts import render


def blogs(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('about')


def cip(request, name):
    return HttpResponse(f"comment for post {name}")


def ufp(request, name):
    return HttpResponse(f"update post {name}")


def dp(request, name):
    return HttpResponse(f"delete post {name}")


def profile(request, username):
    return HttpResponse(f'Profile {username}')


def change_password(request):
    return HttpResponse('Change Password')


def register(request):
    return HttpResponse('register')


def login(request):
    return HttpResponse('log in')


def logout(request):
    return HttpResponse('log out')


def blog_post(request, name):
    return HttpResponse(f'Your post {name}')
