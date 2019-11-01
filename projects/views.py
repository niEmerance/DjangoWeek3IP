# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import RegisterForm,NewProjectForm,ProfileForm,CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import User,Project,Profile
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer



# Create your views here.
@login_required(login_url='login/')
def welcome(request):
    try:
        projects= Project.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'welcome.html',{"projects":projects})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('projects:login')
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('projects:welcome')
    else:
        form=AuthenticationForm()
    return render(request, 'registration/login.html',{"form":form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
    return redirect('projects:login')

@login_required(login_url='login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.prj_uploader = current_user
            post.save()
        return redirect('projects:welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='login/')
def profile_view(request,user_id):
   current_user = request.user.username
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user = current_user
           profile.save()
           return redirect('projects:profile')
   else:
       form = ProfileForm()
   user=User.objects.all()
   prj_image = Project.objects.filter(user__username=current_user)
   profile = Profile.objects.filter(user__username = current_user)
   return render(request,"profile.html",{"user":user,"prj_images":prj_image,"profile":profile})

@login_required(login_url='login/')
def update_profile(request):
   current_user=request.user
   if request.method =='POST':
       if Profile.objects.filter(user_id=current_user).exists():
           form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
       else:
           form=ProfileForm(request.POST,request.FILES)
       if form.is_valid():
         profile=form.save(commit=False)
         profile.user=current_user
         profile.save()
         return redirect('projects:profile',current_user.id)
   else:
       if Profile.objects.filter(user_id = current_user).exists():
          form=ProfileForm(instance =Profile.objects.get(user_id=current_user))
       else:
           form=ProfileForm()
   return render(request,'profile_form.html',{"form":form})

@login_required(login_url='login/')
def comment_view(request,project_id):
   current_user=request.user
   if request.method=='POST':
       project_detail=Project.objects.filter(id=project_id).first()
       form=CommentForm(request.POST,request.FILES)
       if form.is_valid():
           comment=form.save(commit=False)
           comment.username=current_user
           comment.prj_comment=project_detail
           comment.save()
       return redirect('projects:welcome')
   else:
       form=CommentForm()
   return render(request,'comment.html',{"form":form,"project_id":project_id})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

def searchProject(request):
    if 'project' in request.GET and request.GET['project']:
        search_term=request.GET.get('project')
        projects=Project.searchProject(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{'message':message,'projects':projects})
    else:
        message='no search yet'
        return render(request,'search.html',{'message':message})
