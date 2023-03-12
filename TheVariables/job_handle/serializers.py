from .models import JobApplied,JobAvailable,Skill,User,Company
from compony_handle.serializers import CompanySerializer
from accounts.serializers import UserSerializer
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
    

class JobAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAvailable
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['company'] = CompanySerializer(
            Company.objects.get(pk=data['company'])).data
        data['skills'] = SkillSerializer(
            Skill.objects.get(pk=data['skills'])).data
        return data

class JobAppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplied
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(
            User.objects.get(pk=data['user'])).data
        data['applied'] = JobAvailableSerializer(
            JobAvailable.objects.get(pk=data['applied'])).data
        return data