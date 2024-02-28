from django.shortcuts import render
from .models import Profile

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

# Details Page
def profile_details(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/details.html', { 
        'profile': profile
    })