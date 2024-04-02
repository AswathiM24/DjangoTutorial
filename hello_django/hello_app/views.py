from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    return render(request,'hello.html')
