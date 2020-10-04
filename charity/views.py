from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from .models import Category, Institution, Donation, CustomUser
from .forms import RegistrationForm, LoginForm, DonationForm


class LandingPageView(View):
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


class AddDonationView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        ctx = {}
        return render(request, 'form.html', ctx)


class AddDonationConfView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm  

    def form_valid(self, form):
        print(form.cleaned_data)
        user = authenticate(username=form.cleaned_data['login'],
                            password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            return redirect(reverse_lazy('register'))
        return redirect(reverse_lazy('landing-page'))


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy("landing-page"))


class ProfileView(View):
    def get(self, request):
        user = CustomUser.objects.get(pk=self.request.user.id)
        donations = Donation.objects.filter(user_id=user.id)
        categories = Category.objects.all()
        ctx = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'donations': donations,
            'categories': categories,
        }
        return render(request, 'profile.html', ctx)