from django.shortcuts import render
from django.http import HttpResponse
def myfirstview(request):
    return HttpResponse('hola')