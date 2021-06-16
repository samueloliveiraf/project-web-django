from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def login_user(request):
    return render(request, 'login.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(login_user)
    template_name = 'cadastrar.html'
