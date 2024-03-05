from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Profile

# Home View
def home(request):
    return render(request, 'home.html')

# About View
def about(request):
    return render(request, 'about.html')

# Profiles View
def profile_list(request):
    profiles = Profile.objects.all() 
    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })

# Details View
def profile_details(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/details.html', { 
        'profile': profile
    })

# Create View
class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'