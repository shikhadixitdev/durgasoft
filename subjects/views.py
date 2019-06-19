from django.shortcuts import render
from django.http.response import HttpResponse
def home(request):
    x="<h1> Welcome to My First Page in Django</h1>"
    return HttpResponse(x)
def contact(request):
    y="<h1> My Contact no is 9786876757664 in Django</h1>"
    return HttpResponse(y)
def services(request):
    s="<h1>We provided all services in Django</h1>"
    return HttpResponse(s)
def feedback(request):
    f="<h1> We have good feedback in Django</h1>"
    return HttpResponse(f)




# Create your views here.
