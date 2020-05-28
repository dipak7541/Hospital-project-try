from django.db import models

class UserRegistration(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('S','Unspecified')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age=models.IntegerField(null=True)
    address=models.TextField()
    bloodgroup=models.CharField(max_length=5)
    password=models.CharField(max_length=32)
    conformpass=models.CharField(max_length=15)    
    
