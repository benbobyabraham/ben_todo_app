from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_new_todo, name='add'),
    path('done/<todo_id>/', views.done_todo, name='done'),
    path('undone/<todo_id>/', views.undone_todo, name='undone'),
    path('delete/', views.delete_todo, name='delete'),
]
