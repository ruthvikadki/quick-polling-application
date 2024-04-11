from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        ),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
