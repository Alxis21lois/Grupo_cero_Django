from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def andres_lupin(request):
    return render(request,"core/tejedores/andres_lupin.html")