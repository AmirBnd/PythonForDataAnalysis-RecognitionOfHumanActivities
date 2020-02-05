from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # This is a view
    return HttpResponse("You are on the  main page : isn't it beautiful ?")
    
