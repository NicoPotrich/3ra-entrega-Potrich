from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import DeleteView

def index(request):
    todos = Todo.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)

def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)

def edit(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)
    elif request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        messages.success(request, 'Tarea actualizada')
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)

def create(request):
    if request.method == "GET":
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo/create.html', context)
    elif request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')

class Delete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo') 



