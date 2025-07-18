from django.http import JsonResponse
from .supabase_client import supabase

def create_todo(request):
    title = request.GET.get("title", "Untitled Task")
    result = supabase.table("todos").insert({"title": title, "is_complete": False}).execute()
    return JsonResponse({"status": "created", "data": result.data})

def list_todos(request):
    result = supabase.table("todos").select("*").execute()
    return JsonResponse(result.data, safe=False)
