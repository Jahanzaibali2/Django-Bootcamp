from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    # return HttpResponse("This is my HOME page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Project's Author name is Jahanzaib Ali")

def contact(request):
    return HttpResponse("This is my contact 03132656524")