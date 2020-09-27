from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Category, Institution, Donation


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all().count()
        institutions = Institution.objects.all().count()
        foundations = Institution.objects.filter(type=Institution.FUNDACJA)
        organizations = Institution.objects.filter(type=Institution.ORGANIZACJA_POZARZADOWA)
        local_collections = Institution.objects.filter(type=Institution.ZBIORKA_LOKALNA)
        ctx = {
            "donations": donations,
            "institutions": institutions,
            "foundations": foundations,
            "organizations": organizations,
            "local_collections": local_collections
        }
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
