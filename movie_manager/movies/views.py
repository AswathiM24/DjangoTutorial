from django.shortcuts import render
from . models import movieInfo

# Create your views here.
def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('summary')
        movie_obj=movieInfo(title=title,year=year,description=desc)
        movie_obj.save()
    return render(request,'create.html')

def list(request):
    # movie_data={'movies':[{'title':'Aadujeevitham',
    #             'year':2024,
    #             'success':False,
    #             'Summary':'Survival thriller',
    #             'img':'goat.jpeg'},
    #             {'title':'Manjummal boys',
    #             'year':2024,
    #             'Summary':'Survival thriller',
    #             'success':True,
    #             'img':'manjummel.jpeg'}
    #             ]}
    movie_set=movieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set}) 

def edit(request):
    return render(request,'edit.html')
