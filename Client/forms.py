from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from Client.models import Job
from accounts.models import Profile, City

User = get_user_model()


class ClientProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number','address','image')


class ClientSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','image','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.is_customer = True
        user.save()
        return user


class ClientSignUpUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email',]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('Title','country', 'city','content','location','image')

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
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')