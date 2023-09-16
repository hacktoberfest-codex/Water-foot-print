from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def page1(request):
    return render(request,'page1.html')
def resultpage(request):
    return render(request,'result.html')


# Create your views here.
