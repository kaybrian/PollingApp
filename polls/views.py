from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,'polls/index.html',context)

def Create(request):
    context = {}
    return render(request,'polls/create.html',context)

def vote(request):
    context = {}
    return render(request,'polls/vote.html',context)

def result(request):
    context = {}
    return render(request,'polls/result.html',context)