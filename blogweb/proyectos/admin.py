from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('creada','actualizada')
    list_display=('nombre','activa','creada')

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Tag)
admin.site.register(Autor)
admin.site.register(Manual)

# Register your models here.
