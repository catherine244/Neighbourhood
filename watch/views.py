# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'notifications.html', {"notifications":all_notifications})


@login_required(login_url='/accounts/login/')
def blog(request):
    current_user=request.user
    profile = Profile.objects.get(username=current_user)
    blogposts = BlogPost.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'blog.html', {"blogposts":blogposts})

@login_required(login_url='/accounts/login/')
def health(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'health.html', {"healthservices":healthservices})

@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities=Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'authorities.html', {"authorities":authorities})
