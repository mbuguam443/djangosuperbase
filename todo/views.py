from django.shortcuts import redirect, render
from django.conf import settings
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def index(request):
    todos = supabase.table("todos").select("*").execute().data
    return render(request, "todo/index.html", {"todos": todos})

def create_todo(request):
    title = request.GET.get("title", "")
    if title:
        supabase.table("todos").insert({"title": title, "is_complete": False}).execute()
    return redirect("todo_index")

def toggle_todo(request, id):
    todo = supabase.table("todos").select("*").eq("id", id).execute().data[0]
    supabase.table("todos").update({"is_complete": not todo["is_complete"]}).eq("id", id).execute()
    return redirect("todo_index")

def delete_todo(request, id):
    supabase.table("todos").delete().eq("id", id).execute()
    return redirect("todo_index")
