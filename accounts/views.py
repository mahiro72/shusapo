from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm,RegistrationForm

from django.contrib.auth import get_user_model
from django.views import generic

User = get_user_model()


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'



"""アカウント登録ページ"""
class Registration(generic.CreateView):
    model = User
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm
    success_url ='/registration/complete'


"""アカウント登録完了"""
class RegistrationComp(generic.TemplateView):
    template_name = 'accounts/registration_complete.html'

