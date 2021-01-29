from django.contrib import admin

# Register your models here.
from .models import City,Country,Profile
from .models import User
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(User)