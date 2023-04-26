from django.shortcuts import render

def myfirstview(request):
    data={
        'name':'django'
    }
    return render('index.html',request,data)