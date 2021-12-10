from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True,  blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200,  null=True)
    profile_pic = models.ImageField(default="ProfilePicture.png", null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
class Ocr_Note(models.Model):

    ocr_pic = models.ImageField(upload_to='ocr/')