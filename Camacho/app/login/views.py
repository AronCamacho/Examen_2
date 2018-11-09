from django.shortcuts import render
from .forms import FormularioLogin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def loginPage(request):
	if request.method == 'POST':
		formulario = FormularioLogin(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username = usuario,password = clave)
			if user is not None:
				if user.is_active:
						login(request,user)
						#messages.warning(request,'te has autenticado de forma correcta')
						return HttpResponseRedirect(reverse('producto'))
				else:
					messages.warning(request,'Usuario inactivo')
			else:
				messages.warning(request,'usuario y/o contraseña incorrecta')
	else:
		formulario = FormularioLogin()
		context = {
				'f': formulario,
			}
	return render(request,'login/login.html',context)

def logoutPage(request):
	logout(request)
	return HttpResponseRedirect(reverse("home_page"))
