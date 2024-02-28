from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:profile_id>/', views.profile_details, name='details'),
]
