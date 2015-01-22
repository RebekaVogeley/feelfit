from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

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

	


