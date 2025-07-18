from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo_index'),
    path('create/', views.create_todo, name='create_todo'),
    path('toggle/<int:id>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
]
