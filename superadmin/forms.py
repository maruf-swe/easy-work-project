# Super Admin Profile Update Form
from django import forms

from accounts.models import Profile, Country , City
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class SuperAdminProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number','address','image')


class SuperAdminSignUpUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email',]


class SuperAdminCategoryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields =['name']


class SuperAdminSubCategoryForm(forms.ModelForm):
    class Meta:
        model = City
        fields =['country','name']