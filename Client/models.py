from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from accounts.models import Country, City
from django.contrib.auth import get_user_model
User = get_user_model()


class Job(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    city = models.ManyToManyField(City, verbose_name="Sub Category", )
    Title = models.CharField(max_length=100)
    content = models.TextField()
    applied_username = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE,
                                         related_name='applied_username')
    is_apply = models.BooleanField('Apply',null=True,blank=True)
    is_published = models.BooleanField('Published',default=False)
    image = models.ImageField(default='default.jpg', upload_to='job_pics',blank=True,null=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)