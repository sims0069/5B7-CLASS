from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages #messages is imported from dj.lib to display warning, error or welcome messages. note: passing them as context will make them remain static on the page

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome to 5B7, {username}")
            return redirect("/")

    else: 
        form = UserRegistrationForm()
    return render(request, "user/register.html", {"form": form})

def home(request):
    return render(request, 'user/home.html')