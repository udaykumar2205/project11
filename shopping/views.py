from django.shortcuts import render

# Create your views here.

def suite(request):
    return render(request,'suite.html')