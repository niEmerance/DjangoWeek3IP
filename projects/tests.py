# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Profile,Project,Comment
# Create your tests here.

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(profile_pic = 'default.jpg', bio ='Muriuki', contact ='0785236547')
        self.james.save_profile()

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pitch= Project(prj_image= 'default.jpg', prj_title ='Muriuki', prj_link ='www.emy.com')
        self.pitch.save_project()