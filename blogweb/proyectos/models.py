from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=200, verbose_name='Nombre')
    creada=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizada=models.DateTimeField(auto_now=True, verbose_name='Fecha que se actualizo')
    activa = models.BooleanField(default=True, verbose_name='Activa')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre
class Tag(models.Model):
    nombre= models.CharField(max_length=200, verbose_name='Nombre')
    creada=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizada=models.DateTimeField(auto_now=True, verbose_name='Fecha que se actualizo')
    activa = models.BooleanField(default=True, verbose_name='Activa')

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre= models.CharField(max_length=200, verbose_name='Nombre')
    creada=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizada=models.DateTimeField(auto_now=True, verbose_name='Fecha que se actualizo')
    activa = models.BooleanField(default=True, verbose_name='Activa')

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre
class Manual(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Titulo')
    contenido=models.CharField(max_length=200, verbose_name='Contenido')
    publicacion = models.BooleanField(default=True, verbose_name='Publicacion')
    img = models.ImageField(upload_to='posts',null=True,blank=True,verbose_name='Image')

    creada = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')
    actualizada=models.DateTimeField(auto_now=True, verbose_name='Fecha que se actualizo')

    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name='Categoria')
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,verbose_name='Autor')
    Tags = models.ManyToManyField(Tag,verbose_name='etiquetas')

    class Meta:
        verbose_name='Manual'
        verbose_name_plural='Manuales'
        ordering=['titulo']
    
    def __str__(self):
        return self.titulo