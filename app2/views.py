from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to index of app1<h1/>")
def sam1(request):
    return render(request,"app2/sam1.html")