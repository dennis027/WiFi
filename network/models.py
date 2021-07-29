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
    __tablename__ = 'subscriber'

    class Package(models.TextChoices):
        first='30mbps', '30mbps',
        second= '55mbps', '55mbps',
        third='80mbps', '80mbps',
        fourth='125mbps', '125mbps',
            
    
   
    user = models.ForeignKey(User,on_delete= models.CASCADE)  
    package=models.CharField(max_length=255,choices=Package.choices ,default='25mbps')
    location= models.CharField(max_length=100)