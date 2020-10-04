from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import CustomUser
from django import forms


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=56, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=56, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    email = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2',)

    def clean_email(self):
        if CustomUser.objects.filter(email=self.data['email']).exists():
            raise forms.ValidationError("Ten adres email już widniej w naszej bazie!")
        return self.data['email']

    def clean_password(self):
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError('Hasła nie są identyczne!')
        return super().clean()

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class DonationForm(forms.Form):
    pass
