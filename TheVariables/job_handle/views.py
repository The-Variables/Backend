from django.shortcuts import render
from .serializers import JobAppliedSerializer,JobAvailableSerializer,SkillSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import JobApplied,JobAvailable,Skill
from django.contrib.sites.models import Site
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
class JobAppliedAPI(viewsets.ModelViewSet):
    serializer_class = JobAppliedSerializer
    queryset = JobApplied.objects.all()

class JobAvailableAPI(viewsets.ModelViewSet):
    serializer_class = JobAvailableSerializer
    queryset = JobAvailable.objects.all()

class SkillAPI(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()    

class SendInterviewAPI(APIView):
    def post(self, request):
        email = 'hphemant373@gmail.com'
        try:
            subject = 'Your Interview Has been finalized'
            message = f'Hi!\nHemant Singh, Congratulations,your application has been reviewed and selected for an interview at Google\nYour interview has been scheduled on 12th March at 6:09pm\n Your Meeting link: https://sweet-hamster-b6fea3.netlify.app'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return Response({'status': 200,'message' : 'Please Check Your Mail, an Email verfication link has been provided'})
        except Exception as e:
            return Response({'status': 405, 'error': str(e) ,'message': 'Sorry Some error has occured, Please try again after sometime'})
