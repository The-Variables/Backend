from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyAPI

router = DefaultRouter()
router.register('company', CompanyAPI, 'company-api')

urlpatterns = [
    path('', include(router.urls))
]