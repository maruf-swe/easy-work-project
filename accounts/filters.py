from django.contrib.auth.models import User
import django_filters
from django import forms

from django.contrib.auth import get_user_model
from Client.models import Job

User = get_user_model()


class JobFilter(django_filters.FilterSet):

    class Meta:
        model = Job
        fields = ['country']



