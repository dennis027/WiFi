from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    bio=models.TextField()
    pic=models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User, related_name='profile',on_delete= models.CASCADE)
    def __str__(self):
        return self.bio   

class Subscriber(models.Model):
    class Units(models.TextChoices):

        KG ='KG','kg'
        L='L','l'
    user = models.ForeignKey(User,on_delete= models.CASCADE)  
    package= models.IntegerField(choices=Units.choices,default=Units.KG) 
    location= models.CharField(max_length=100)