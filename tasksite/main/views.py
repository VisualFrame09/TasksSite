from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    context={
        'title':'Главная страница',
    }
    return render(request,'main/index.html',context=context)

def about(request):
    return render(request,"main/about.html")

def tasks(request):
    context={
        'tasks':Task.objects.order_by('-id'),
    }
    return render(request,'main/tasks.html',context=context)

def create(request):
    error=''
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error="Введенные данные некорректны"
    form=TaskForm()
    context={
        'form':form,
        'error':error,
    }
    return render(request,'main/create.html',context=context)