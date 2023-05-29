"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.admin import register
from django.db import models
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import User
from . import User
from django.urls import path
import music.views


class RegistrationForm:
    pass


class UploadMusicForm:
    pass


class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    ACCESS_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='music_files/')
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES, default=PUBLIC)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    allowed_emails = models.ManyToManyField(User, related_name='allowed_music_files', blank=True)

    def __str__(self):
        return self.title

    def register(self):
        if self.method == 'POST':
            form = RegistrationForm(self.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(self, 'music/register.html', {'form': form})

    def user_login(self):
        if self.method == 'POST':
            email = self.POST['email']
            password = self.POST['password']
            user = authenticate(self, email=email, password=password)
            if user is not None:
                login(self, user)
                return redirect('homepage')
            else:
                return render(self, 'music/login.html', {'error': 'Invalid credentials'})
        return render(self, 'music/login.html')

    def upload_music(self):
        if self.method == 'POST':
            form = UploadMusicForm(self.POST, self.FILES)
            if form.is_valid():
                music_file = form.save(commit=False)
                music_file.uploaded_by = self.user
                music_file.save()
                return redirect('homepage')
        else:
            form = UploadMusicForm()
        return render(self, 'music/upload.html', {'form': form})

    def homepage(self):
        music_files = MusicFile.objects.filter(
            models.Q(access=MusicFile.PUBLIC) | models.Q(uploaded_by=self.user) | models.Q(
                allowed_emails=self.user))
        return render(self, 'music/homepage.html', {'music_files': music_files})


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('upload/', upload_music, name='upload'),
    path('homepage/', homepage, name='homepage'),
]
