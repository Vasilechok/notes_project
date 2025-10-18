from django.urls import path
from .views import NoteListView, NoteDetailView, create_note

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('create/', create_note, name='create_note'),
]
