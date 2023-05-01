from django.shortcuts import render

def proyectolist(request):
    data ={

    }
    return render(request,'proyectos/listar.html',data)