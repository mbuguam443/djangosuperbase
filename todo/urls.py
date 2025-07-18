from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_todo),
    path('list/', views.list_todos),
]
