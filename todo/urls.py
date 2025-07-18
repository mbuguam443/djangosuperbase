from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='todo_index'),
    path("login/", views.login_view, name="login"),
    path('create/', views.create_todo, name='create_todo'),
    path('toggle/<int:id>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_image, name='upload_image'),
]
