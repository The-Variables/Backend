from django.db import models
from compony_handle.models import Company
from accounts.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=120, help_text='Enter_skill_name')

    def __str__(self):
        return self.name

class JobAvailable(models.Model):
    company = models.ForeignKey(Company, related_name='company_job_available', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, help_text='Enter_job_name')
    skills = models.ManyToManyField(Skill)
    vacancies = models.IntegerField(help_text='Number_of_vacancies_available')
    def __str__(self):
        return self.name +', '+self.company.name


class JobApplied(models.Model):
    user = models.ForeignKey(User, related_name='applied_user', on_delete=models.CASCADE)
    applied = models.ForeignKey(JobAvailable, related_name='job_user_applied', on_delete=models.CASCADE)
    resume = models.FileField(help_text='Submit Resume',upload_to = 'UserResume/')
    def __str__(self):
        return self.user.username +'\'s '+ self.applied.name