from functools import wraps
from django.shortcuts import redirect

def login_required_supabase(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.session.get("user")
        if not user:
            return redirect("/login/")
        return view_func(request, *args, **kwargs)
    return wrapper
