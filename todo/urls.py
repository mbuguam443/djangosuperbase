from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_todo),
    path("", views.list_todos),  # ← This handles /todo/
]
