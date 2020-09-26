from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


class LandingPage(View):
    def get(self, request):
        ctx = {}
        return render(request, 'index.html', ctx)


class AddDonation(View):
    def get(self, request):
        ctx = {}
        return render(request, 'form.html', ctx)


class Login(View):
    def get(self, request):
        ctx = {}
        return render(request, 'login.html', ctx)


class Register(View):
    def get(self, request):
        ctx = {}
        return render(request, 'register.html', ctx)
