from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import AuthenticationForm, LoginView


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/menu.html')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/profile.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'hyperjob/signup.html'






