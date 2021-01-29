from django.contrib.auth.models import User
import django_filters

from django.contrib.auth import get_user_model

from Client.models import Job
from accounts.models import Profile, City

User = get_user_model()


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = City
        fields = ['country']


class ActiveFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['is_active']


class PublishedFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['is_published']