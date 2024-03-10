from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import DeleteView

def index(request):
    meeting = Meeting.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'meeting': meeting
    }
    return render(request, 'meetings/index.html', context)

def view(request, id):
    meeting = Meeting.objects.get(id=id)
    context = {
        'meeting': meeting
    }
    return render(request, 'meetings/detail.html', context)

def edit(request, id):
    meeting = Meeting.objects.get(id=id)

    if request.method == 'GET':
        form = MeetingForm(instance=meeting)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'meetings/edit.html', context)
    elif request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
        messages.success(request, 'Reunion actualizada')
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'meetings/edit.html', context)

def create(request):
    if request.method == "GET":
        form = MeetingForm()
        context = {
            'form': form
        }
        return render(request, 'meetings/create.html', context)
    elif request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('meetings')

class Delete(DeleteView):
    model = Meeting
    success_url = reverse_lazy('meetings') 
