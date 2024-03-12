from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'base/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'base/updatetask.html', context)

def delete(request, pk):
    item = Task.objects.get(id=pk)

    context = {'item':item}

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'base/deleteitem.html', context)