from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreatingForm


class SignUpView(CreateView):
    form_class = CustomUserCreatingForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")