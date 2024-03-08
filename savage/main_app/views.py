from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Profile
from django import forms

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

# Define the ProfileForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all() 

    def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            self.fields['user'].required = True
            self.fields['user'].empty_label = None
            self.fields['user'].queryset = User.objects.all()

# Create View
class ProfileCreate(CreateView):
    model = Profile
    form_class = ProfileForm  # Use the custom ProfileForm
    success_url = '/profiles/'

    def form_valid(self, form):
        profile = form.save()
        return redirect('details', profile_id=profile.id)