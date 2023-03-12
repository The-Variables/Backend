from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobAppliedAPI,JobAvailableAPI,SkillAPI,SendInterviewAPI

router = DefaultRouter()
router.register('job-available', JobAvailableAPI, 'job-available-api')
router.register('skill', SkillAPI, 'skill-api')
router.register('job-applied', JobAppliedAPI, 'job-applied-api')

urlpatterns = [
    path('', include(router.urls)),
    path('send-interview/', SendInterviewAPI.as_view(),name='send-interview'),
]