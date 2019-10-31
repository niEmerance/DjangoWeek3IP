# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profiles/')
    bio = models.TextField(max_length =100)
    contact=models.IntegerField(default=None, null=True)

    def __str__(self):
        return self.bio

class Project(models.Model):
    prj_title = models.CharField(max_length =30)
    prj_image = models.ImageField(upload_to = 'photos/')
    prj_desc= models.CharField(max_length=300)
    prj_link =models.URLField()
    prj_uploader = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.prj_title

    def save_project(self, user):
        self.save()
    @classmethod
    def searchProject(cls,search_term):
        prj=cls.objects.filter(prj_title__icontains=search_term)
        return prj
    @classmethod
    def get_all_projects(cls):
       projects=cls.objects.all().prefetch_related('comment_set')
       return projects

class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prj_comment = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.username

    def save_comment(self):
        self.save()
