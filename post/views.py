from django.shortcuts import render,redirect
from .models import post

def home(request):
    posts=post.objects.all()
    return render(request,'home.html',{'posts':posts})
def posts(request,pk):
    posts=post.objects.get(id=pk)
    
    return render(request,'post.html',{'post':posts})