from django.contrib import admin
from .models import Producto
class AdminProducto(admin.ModelAdmin):
	list_display = ["codigo","nombre","categoria","marca","precio","descripcion"]
	list_editable = ["nombre","precio"]
	list_filter = ["precio"]
	search_fields= ["codigo","nombre","precio"]


	class Meta:
		model = Producto

admin.site.register(Producto,AdminProducto)
