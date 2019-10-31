from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields = ('profile_pic', 'bio', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields = ('prj_title', 'prj_desc', 'prj_link')