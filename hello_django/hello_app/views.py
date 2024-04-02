from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    movie_list={'title':'Aadujeevitham',
                'year':2024,
                'Summary':'Survival thriller'}
    return render(request,'hello.html',movie_list)
