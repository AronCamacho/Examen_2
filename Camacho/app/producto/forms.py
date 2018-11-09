from django import forms
from app.modelo.models import Producto

class FormularioProducto(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ["codigo","nombre","categoria","marca","precio","descripcion"]