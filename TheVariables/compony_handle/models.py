from django.db import models

# Create your models here.
class Company(models.Model):
    bio = models.CharField(null=True, blank=True,max_length=120, help_text='Enter company bio')
    photo = models.ImageField(null=True, blank=True,help_text='Enter Company Profile photo' , upload_to='CompanyPhoto/')
    logo = models.ImageField(null=True, blank=True,help_text='Enter Company logo' , upload_to='CompanyLogo/')
    date_of_establishment = models.DateField()
    name = models.CharField(max_length=120, help_text = 'Enter Company name')

    def __str__(self):
        return self.name