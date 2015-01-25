# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm

def home(request):
    return render(request, 'index.html')

def login_view(request):
	
	template_name = 'login.html'

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				return redirect('home')
			else:
				return redirect('error_page')
		else:
			messages.warning(request, 'Login inválido ou vazio')
			return redirect('home')

	return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('home')

def exercicios(request):
	return render(request,'exercicios.html')

def dietas(request):
	return render(request,'dietas.html')

def ganhar_massa(request):
	return render(request,'ganhar_massa.html')

def sobrenos(request):
	return render(request,'sobrenos.html')

def dicas(request):
	return render(request,'dicas.html')	

def calculoimc(request):
	return render(request,'calculoimc.html')	

def perder_peso(request):
	return render(request,'perder_peso.html')	

	
def cadastrar(request):
	template_name = 'cadastrar.html'

	if request.method == 'POST':

		form = RegisterForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			return redirect('home')
		else:
			form = RegisterForm(request.POST)
	else:
		form = RegisterForm()
	context = {
		'form': form
	}

	return render(request, template_name, context)
