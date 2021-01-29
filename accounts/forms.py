from django import forms

from Client.models import Job
from .models import Profile, City
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class AppliedForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['is_apply']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_apply = True
        user.save()
        return user


# Worker Registration Form
class WorkerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','image', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.is_worker = True
        user.save()
        return user


# Worker Registration User  Update
class WorkerSignUpUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email',]


class PersonForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('country', 'city','phone_number','address','image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields["city"].widget = forms.widgets.CheckboxSelectMultiple()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.country:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')