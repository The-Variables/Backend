from django.contrib import admin
from .models import Skill, JobApplied, JobAvailable
# Register your models here.

admin.site.register(Skill)
admin.site.register(JobApplied)
admin.site.register(JobAvailable)
