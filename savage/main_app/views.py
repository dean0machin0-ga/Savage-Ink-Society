from django.shortcuts import render
from .models import Profile  # Import the Profile model

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Profiles Page
def profile_list(request):
    profiles = Profile.objects.all() 
    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })
