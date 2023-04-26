from django.urls import path
from .views import myfirstview
urlpatterns = [
    path('proyectos/',myfirstview),
]
