
#YEv View page bhi django ne nahi maine banai he bhai....


from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')