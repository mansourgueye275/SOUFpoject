from django.contrib.gis.db import models

from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField(max_length=255,null=False,blank=False)
    surname=models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(max_length=255, unique=True,null=False)
    telephone=models.IntegerField(max_length=15,null=False)
    #	password	field	defined	in	base	class
    objects=models.GeoManager


    USERNAME_FIELD = 'email'

    @classmethod
    def get_by_id(cls, uid):
        return User.objects.get(pk=uid)

    def __str__(self):
        return self.email