from django.db import models

# Create your models here.
class Users(models.Model):
    user_name= models.CharField(max_length=100,default="")
    user_fname= models.CharField(max_length=100,default="")
    user_age= models.IntegerField(default=0)
    user_address= models.CharField(max_length=300,default="")
    user_country= models.CharField(max_length=100,default="")
    def __str__(self):
        return self.user_name