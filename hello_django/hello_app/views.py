from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    movie_data={'movies':[{'title':'Aadujeevitham',
                'year':2024,
                'success':False,
                'Summary':'Survival thriller'},
                {'title':'Manjummal boys',
                'year':2024,
                'Summary':'Survival thriller',
                'success':True}
                ]}
    return render(request,'hello.html',movie_data)
