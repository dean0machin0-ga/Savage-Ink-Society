from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first = models.CharField(max_length=50, blank=True)
    last = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    astrological_sign = models.CharField(max_length=50, blank=True)

    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        else:
            return None
        
    def __str__(self):
        return self.user.username if self.user else "No User"
    
    # def __str__(self) :
    #     return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('details', kwargs={'profile_id': self.id})

class TattooShop(models.Model):
    name = models.CharField(max_length=250)
    price_range = models.CharField(max_length=10, blank=True, null=True)
    rating = models.FloatField()
    review_count = models.IntegerField()
    address = models.TextField
    phone = models.IntegerField()
    business_link = models.URLField()
    photo = models.URLField

class Pics(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)