from django.shortcuts import render
from django.http import HttpResponse
def myfirstview(request):
    persona={
        'name':'leandro'
    }
    return render(request,'home.html',persona)