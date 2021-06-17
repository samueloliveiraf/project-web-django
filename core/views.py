from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválida")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')


def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)

    evento = Evento.objects.filter(usuario=usuario).values(
        'id', 'usuario', 'titulo', 'data_criacao')
    return JsonResponse(list(evento), safe=False)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(login_user)
    template_name = 'cadastrar.html'
