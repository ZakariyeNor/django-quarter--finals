from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_blog(request):
    if request.method == "POST":
        return HttpResponse("You Posted")
    elif request.method == "GET":
        return HttpResponse("You got the data")