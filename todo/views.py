from django.shortcuts import render, redirect
from supabase import create_client
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_ANON_KEY"))

def todo_list(request):
    todos = supabase.table("todos").select("*").execute().data
    return render(request, "todo/todo_list.html", {"todos": todos})

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            supabase.table("todos").insert({"title": title}).execute()
        return redirect("todo_list")
    return render(request, "todo/add_todo.html")
