from django.shortcuts import render

# Create your views here.

def lifecare(request):
    return render(request,'index.html')