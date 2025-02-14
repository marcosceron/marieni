from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django 
from django.shortcuts import redirect
from django.contrib.auth import logout as logout_django

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.filter(username=username).first()
        
        if user:

            return HttpResponse('Já existre um usuario com esse nome')
       
        user = User.objects.create_user(username=username, email=email, password=senha, first_name=first_name, last_name=last_name )
        user.save()

        return HttpResponse('usuario cadastrado com sucesso.')

def logout(request):
    logout_django (request)
    return redirect('login')
def login (request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else: 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            request.session['username'] = username
            request.session['first_name'] = user.first_name
            request.session.save()
            return redirect('index')
            
        else:
            return HttpResponse('Email ou senha inválidos.')
        
def index (request): 
    return render (request, 'index.html')