from django.shortcuts import render
from django.http import HttpResponse
def myfirstview(request):
    return render(request,'index.html')