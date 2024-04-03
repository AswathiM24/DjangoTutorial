from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
    return render(request,'create.html')

def list(request):
    movie_data={'movies':[{'title':'Aadujeevitham',
                'year':2024,
                'success':False,
                'Summary':'Survival thriller',
                'img':'goat.jpeg'},
                {'title':'Manjummal boys',
                'year':2024,
                'Summary':'Survival thriller',
                'success':True,
                'img':'manjummel.jpeg'}
                ]}
    return render(request,'list.html',movie_data) 

def edit(request):
    return render(request,'edit.html')
