from django.shortcuts import render, redirect

from django.http import HttpResponse
from app.modelo.models import Producto
from .forms import FormularioProducto
from django.contrib.auth.decorators import login_required


@login_required
def principal(request):
	lista= Producto.objects.all()
	context = {
		'lista':lista,

	}


	return render(request,'producto/principal_cliente.html',context)
	#return HttpResponse('Es el index del cliente')

def crear(request):
		formulario = FormularioProducto(request.POST)
		if request.method == 'POST':
			if formulario.is_valid():
				datos = formulario.cleaned_data
				producto = Producto()
				producto.codigo= datos.get('codigo')
				producto.nombre = datos.get('nombre')
				producto.categoria = datos.get('categoria')
				producto.marca = datos.get('marca')
				producto.precio = datos.get('precio')
				producto.descripcion = datos.get('descripcion')
				producto.save()
				return redirect(principal)
		context = {
			'f':formulario
		}


		return render(request,"producto/crear_cliente.html",context)
