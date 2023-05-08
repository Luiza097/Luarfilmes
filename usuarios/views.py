from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256
    

# Create your views here.

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    number = request.POST.get('number')
    password = request.POST.get('password')

    usuario = Usuario.objects.filter(email = email)

    if len(first_name.strip()) == 0 or len(last_name.strip()) == 0 or len(password.strip()) == 0:
        return redirect('/auth/cadastrar/?status=1')

    if len(password) < 8:
        return redirect('/auth/cadastrar/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastrar/?status=3')
    
    try:
        password = sha256(password.encode()).hexdigest()
        usuario = Usuario(nome = first_name +' '+last_name, email = email, numero = number, senha = password)
        usuario.save()

        return redirect('/auth/cadastrar/?status=0')

    except:
        return redirect('/auth/cadastrar/?status=4')

def valida_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = sha256(password.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = password)

    if len(usuario) == 0:
        return redirect('auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/')

def sair(request):
    request.session.flush()
    return redirect('/')