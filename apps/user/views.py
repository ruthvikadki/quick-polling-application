from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm, SignupForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login, logout


class IsUserAuthenticatedMixin:
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("polls:home")
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


class LoginView(IsUserAuthenticatedMixin, generic.TemplateView):
    template_name = "accounts/auth-signin.html"
    form_class = LoginForm

    def get(self, request):
        return render(
            request,
            template_name=self.template_name,
            context={"form": self.form_class()},
        )

    def post(self, request):
        form = self.form_class(request.POST)
        print(form.errors)

        if form.is_valid():
            print("is valid")

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("polls:home")
            else:
                message = "Invalid credentials"
        print("failed login")
        print(user)

        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class SignupView(IsUserAuthenticatedMixin, generic.CreateView):
    template_name = "accounts/auth-signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("user:login")

class UserLogoutView(LogoutView):
    next_page = "user:login"
