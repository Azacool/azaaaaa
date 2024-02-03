from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def blog(request):
    return render(request,'blog.html',{})

def services(request):
    return render(request,'services.html',{})

def work(request):
    return render(request,'work.html',{})


def contact(request):
    return render(request,'contact.html',{})

