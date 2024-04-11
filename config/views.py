from django.shortcuts import redirect
from django.views.generic import View

class LoginRedirectView(View):
    def get(self, request):
        return redirect("user:login")