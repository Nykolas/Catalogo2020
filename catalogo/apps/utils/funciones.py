from django.core.exceptions import PermissionDenied

class PermisosMixin:
	rol = None
	def dispatch(self,request,*args,**kwargs):
		if check(request,self.rol):
			return super().dispatch(request,*args,**kwargs)
		else:
			raise PermissionDenied

def decoradorPermisos():
	pass

def check(request,rol):
	u = request.user
	if u.mayorista and rol == 'mayorista':
		return True
	elif not (u.mayorista) and rol == 'minorista':
		return True
	else:
		return False
