from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from django.dispatch import receiver #add this
from django.db.models.signals import post_save 

# Create your models here.
class Profile(models.Model):
    bio=models.TextField()
    pic=models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User, related_name='profile',on_delete= models.CASCADE)
    def __str__(self):
        return self.bio   

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
	    instance.profile.save()

    

class Subscriber(models.Model):
    class Units(models.TextChoices):

        KG ='KG','kg'
        L='L','l'
        First= '5000','5000'
    user = models.ForeignKey(User,on_delete= models.CASCADE)  
    package= models.IntegerField(choices=Units.choices,default=Units.KG) 
    location= models.CharField(max_length=100)