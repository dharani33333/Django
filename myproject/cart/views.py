from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def homepage(request):
#    print(request,"----------------")
#    return HttpResponse("<h1>This is HTML page</h1>")

def html(request):
   return render(request,"index.html")