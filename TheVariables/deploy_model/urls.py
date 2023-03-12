from .views import SkillExtractor, SentimentalModelAPI
from django.urls import path

urlpatterns = [
    path('skill-extractor/', SkillExtractor.as_view(), name = 'skill-extractor'),
    path('sentimental/', SentimentalModelAPI.as_view(), name = 'sentimenat-model'),
]