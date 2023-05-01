from django.urls import path
from proyectos.views.proyecto import proyectolist
urlpatterns = [
    path('manuales/listar',proyectolist),
]
