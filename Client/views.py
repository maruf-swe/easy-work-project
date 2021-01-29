from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from accounts.filters import JobFilter
from .models import Job
from accounts.models import Profile, City
from .forms import ClientSignUpForm,ClientSignUpUpdateForm,ClientProfileUpdateForm,JobForm
from django.contrib.auth.views import (
     PasswordChangeView as BasePasswordChangeView,
)
User = get_user_model()


def Clientprofile(request):
    return render(request,'Client/client_profile.html')


def ClientCreateView(request):
    if request.method == 'POST':
        u_form = ClientSignUpForm(request.POST or None, request.FILES or None)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been created! You are waiting for approval')
            return redirect('login')
    else:
        u_form = ClientSignUpForm()

    context = {
            'u_form': u_form,

        }
    return render(request, 'Client/client_reg.html', context)


# Super Admin profile Update

def ClientUserUpdateView(request, pk):
    person = get_object_or_404(User, pk=pk)
    form = ClientSignUpUpdateForm(instance=person)
    if request.method == 'POST':
        form = ClientSignUpUpdateForm(request.POST,request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('client_profile')
    return render(request, 'Client/client_basic_update.html', {'form': form})


# Client profile Update

def ClientProfileCreateView(request):
    form = ClientProfileUpdateForm()
    if request.method == 'POST':
        form = ClientProfileUpdateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('client_profile')
    return render(request, 'client/client_profile_create.html', {'form': form})


# Client profile Update

def ClientProfileUpdateView(request, pk):
    person = get_object_or_404(Profile, pk=pk)
    form = ClientProfileUpdateForm(instance=person)
    if request.method == 'POST':
        form = ClientProfileUpdateForm(request.POST,request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('client_profile')
    return render(request, 'client/client_profile_create.html', {'form': form})


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'Client/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('login')


def JobView(request):
    job = Job.objects.all()
    MyFilter = JobFilter(request.GET, queryset=job)
    job = MyFilter.qs
    context = {
        'job': job,
        'MyFilter': MyFilter,
    }
    return render(request, 'Client/job_list.html', context)


# Job Post Create

def JobCreateView(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            return redirect('job_list')
    return render(request, 'Client/home.html', {'form': form})


# JOb Post Update
@login_required()
def JobUpdateView(request, pk):
    person = get_object_or_404(Job, pk=pk)
    form = JobForm(instance=person)
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    return render(request, 'Client/home.html', {'form': form})


class JobDelete(DeleteView):
    model = Job
    template_name = 'Client/job_delete.html'
    success_url = 'http://127.0.0.1:8000/client/Client/Job/List/'


# Worker Service AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'Client/city_dropdown_list_options.html', {'cities': cities})


def Applied_Job_View(request):
    job = Job.objects.all().filter(is_apply=True)
    MyFilter = JobFilter(request.GET, queryset=job)
    job = MyFilter.qs
    context = {
        'job': job,
        'MyFilter': MyFilter,
    }
    return render(request, 'Client/applied_job.html', context)