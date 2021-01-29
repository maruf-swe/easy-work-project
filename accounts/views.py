from django.contrib.auth import get_user_model, login
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Client.models import Job
from .filters import JobFilter
from .forms import PersonForm,WorkerSignUpForm,WorkerSignUpUpdateForm,AppliedForm
from .models import Profile, City, Country
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.auth.views import (
     PasswordChangeView as BasePasswordChangeView,
)


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('superadminprofile')
        elif request.user.is_worker:
            return redirect('profile')
        elif request.user.is_customer:
            return redirect('client_profile')
    return HttpResponse("login failed")


# def base(request):
#     return render(request,'home.html')

def base(request):
    worker = User.objects.all().filter(is_worker=True)[0:4]
    category = Country.objects.all()
    job = Job.objects.all()[0:4]
    context = {
        'worker': worker,
        'category': category,
        'job': job,

    }
    return render(request,'home.html',context)


def signup(request):
    return render(request,'accounts/signup.html')


def Applied_Job_View(request):
    job = Job.objects.all().filter(is_apply=True)
    return render(request, 'accounts/applied_job.html', {'job': job})


def JobView(request):
    job = Job.objects.all()
    MyFilter = JobFilter(request.GET, queryset=job)
    job = MyFilter.qs
    context = {
        'job': job,
        'MyFilter': MyFilter,
    }
    return render(request, 'accounts/job_post_view_base.html', context)


# Job Post Client VIEW as Home Page
def JobPostView(request,pk):
    person = get_object_or_404(Job, pk=pk)
    person.applied_username = request.user
    person.is_apply = True
    person.save()
    return redirect('job_base')


# Worker Profile view
def workerprofile(request):
    return render(request, 'accounts/profile.html')


def workerprofileviewhome(request):
    worker = User.objects.all().filter(is_worker = True)
    return render(request,'accounts/worker_profile_view_base.html',{'worker':worker})


# Worker Basic Registration
def WorkerCreateView(request):
    if request.method == 'POST':
        u_form = WorkerSignUpForm(request.POST or None, request.FILES or None)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been created! You are waiting for approval')
            return redirect('login')
    else:
        u_form = WorkerSignUpForm()

    context = {
            'u_form': u_form,

        }
    return render(request, 'accounts/worker_reg.html', context)


# Worker Basic Information Update
def WorkerUpdateView(request, pk):
    person = get_object_or_404(User, pk=pk)
    u_form = WorkerSignUpUpdateForm(instance=person)
    if request.method == 'POST':
        u_form = WorkerSignUpUpdateForm(request.POST or None, request.FILES or None, instance=person)
        if u_form.is_valid():
            u_form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'accounts/worker_reg.html', {'u_form': u_form})


# Worker Service Create
def PersonCreateView(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('service_add')
    return render(request, 'accounts/home.html', {'form': form})


# Worker Service Update
def PersonUpdateView(request, pk):
    person = get_object_or_404(Profile, pk=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST,request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('service_change', pk=pk)
    return render(request, 'accounts/home.html', {'form': form})


# Worker Service AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'accounts/city_dropdown_list_options.html', {'cities': cities})


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'accounts/password_change.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('login')


def SingleProfile(request,pk):
    profile = User.objects.filter(pk=pk)
    context = {
        'profile': profile,
    }
    return render(request,'accounts/profile_list.html',context)


def JobSingleDetails(request,pk):
    job = Job.objects.filter(pk=pk)
    context = {
        'job': job,
    }
    return render(request,'accounts/job_list.html',context)