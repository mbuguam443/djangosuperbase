from django.shortcuts import redirect, render
from django.conf import settings
from supabase import create_client
from dotenv import load_dotenv
import os
from todo.login_required_supabase import login_required_supabase

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)



def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = supabase.auth.sign_in_with_password({"email": email, "password": password})
            request.session['user'] = user.user.id  # store user id in session
            print("login success")
            return redirect("todo_index")
        except Exception as e:
            print("server failed")
            return render(request, "auth/login.html", {"error": str(e)})
    return render(request, "auth/login.html")

@login_required_supabase
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

def logout_view(request):
    if "supabase_session" in request.session:
        request.session.flush()
        
    return redirect("/login/")

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        file = request.FILES["image"]
        file_name = "public/"+file.name
        file_data = file.read()

        # Upload to Supabase Storage
        response = supabase.storage.from_("images").upload(file_name, file_data, {"content-type": file.content_type})

        

        public_url = supabase.storage.from_("images").get_public_url(file_name)

        return render(request, "upload_result.html", {"image_url": public_url})
    
    return render(request, "upload_image.html")    

