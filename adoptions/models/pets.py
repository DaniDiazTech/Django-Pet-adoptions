'''Pet model'''

from django.db import models

from adoptions.utils import BaseModel

class Pet(BaseModel):
    
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ] 
     
    name = models.CharField(max_length=100)

    submitter = models.CharField(max_length=100)

    species = models.CharField(max_length=30)

    breed = models.CharField(max_length=30, blank=True)

    sex = models.CharField(max_lenght=1, choices=SEX_CHOICES)

