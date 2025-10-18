from django import forms
from .models import Note
from django.shortcuts import render, redirect


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})
