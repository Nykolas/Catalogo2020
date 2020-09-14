from django.shortcuts import render
from apps.mayorista.models import Mayorista

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


