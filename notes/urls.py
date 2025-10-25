from django.urls import path
from .views import NoteListView, NoteDetailView, create_note
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', NoteListView.as_view(), name='task_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='task_detail'),
    path('create/', create_note, name='create_note'),
    path('register/', views.register, name='register'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
