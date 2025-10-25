from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Class-based views
class NoteListView(ListView):
    model = Note
    template_name = 'tasks/task_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'tasks/task_detail.html'


# Function-based view для створення нотатки
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = NoteForm()

    return render(request, 'tasks/task_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

