from PIL import Image
from django.contrib import auth
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    image = models.ImageField('Voter ID Image', default='default.jpg', upload_to='voter_id_pics', null=True, blank=True)

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    birthdate = models.DateField('Birth Day',null=True, blank=True)
    country = models.ForeignKey(Country,verbose_name="Category", on_delete=models.SET_NULL, null=True)
    city = models.ManyToManyField(City,verbose_name="Sub Category",)
    phone_number = models.CharField('Phone Number', max_length=12, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)