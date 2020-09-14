from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import AltaProducto, ModificacionProducto
from .models import Producto, Rubro
from apps.utils.funciones import PermisosMixin
# VISTA BASADA EN FUNCIONES
#def Listar(request):
#	return render(request,'productos/listar.html')


# VISTAS BASADAS EN CLASES
class Crear(LoginRequiredMixin,PermisosMixin, CreateView):
	rol = 'minorista'
	model = Producto
	form_class = AltaProducto
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('home')

class Modificar(UpdateView):
	model = Producto
	form_class = ModificacionProducto
	template_name = 'productos/modificar.html'
	success_url = reverse_lazy('home')

class Eliminar(DeleteView):
	model = Producto
	success_url = reverse_lazy('productos:listar')

#MOSTRAR TODOS EN CLASS VIEW
class ListarProductos(ListView):
	model = Producto
	template_name = 'productos/listar.html'


#MOSTRAR TODOS EN FUNCTION VIEW
@login_required
def ListarProductosFuncion(request):
	context = {}
	todos = Producto.objects.all()
	context['productos'] = todos

	return render(request,'productos/listar_funcion.html',context)


def Filtros(request):
	context = {}
	rubros = Rubro.objects.all()
	context['rubros'] = rubros
	id_rubro = request.GET.get('filtro',None)

	if id_rubro:
		resultado = Producto.objects.filter(rubro = id_rubro)
		context['productos'] = resultado
	else:
		todos = Producto.objects.all()
		context['productos'] = todos

	return render(request,'productos/filtros.html',context)