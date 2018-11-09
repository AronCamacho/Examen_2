from django.urls import path

from . import views

urlpatterns = [

	path('',views.principal,name = 'producto' ),
	path('crear',views.crear),

]