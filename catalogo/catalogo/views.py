from django.shortcuts import render
from django.http import HttpResponse, Http404
from apps.mayorista.models import Mayorista
from apps.productos.models import Producto

import json
def Home(request):
	# u = request.user
	# if u.is_authenticated:
	# 	if u.mayorista:
	# 		print(u.usuario_mayorista.cuit)
	# 		perfil = Mayorista.objects.get(usuario = u)
	# 		print(perfil.cuit)
	return render(request,'home.html')

def Contacto(request):
	return render(request,'contacto.html')

def Primavera(request):
	ctx = {'c':[1,2,3,4,5]}
	return render(request,'primavera.html',ctx)


def AJAX(request):

	if request.is_ajax():

		valorBuscado = request.GET.get('buscando',None)

		resultado = Producto.objects.filter(nombre__icontains = valorBuscado ) | Producto.objects.filter(descripcion__icontains = valorBuscado )
		respuesta = list()
		if resultado:
			for x in resultado:
				dic = {}
				dic['nombre'] = x.nombre
				dic['descripcion'] = x.descripcion
				dic['precio'] = int(x.precio)
				respuesta.append(dic)
			salida = {'datos':respuesta,'estado':'ok'}
		else:
			salida = {'estado':'mal'}

		data = json.dumps(salida)
		return HttpResponse(data, 'application/json')

	else:
		raise Http404


#[{'nombre':'yerba','precio':200},{},{}]