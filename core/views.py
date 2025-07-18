# core/views.py
from django.http import JsonResponse
from supabase_client import supabase

def test_connection(request):
    try:
        supabase.auth.get_user()  # Light API call
        return JsonResponse({"status": "✅ Supabase connected successfully"})
    except Exception as e:
        return JsonResponse({"status": "❌ Supabase connection failed", "error": str(e)})
