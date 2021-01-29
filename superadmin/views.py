from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,CreateView,DetailView,DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from Client.models import Job
from accounts.models import Profile, Country, City
from .filters import CategoryFilter,ActiveFilter,PublishedFilter
from .forms import SuperAdminProfileUpdateForm,SuperAdminSignUpUpdateForm,SuperAdminCategoryForm,SuperAdminSubCategoryForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login

User = get_user_model()
from django.contrib.auth.views import (
     PasswordChangeView as BasePasswordChangeView,
)

@login_required()
def job_pending_list(request):
    job = Job.objects.all()
    MyFilter = PublishedFilter(request.GET, queryset=job)
    job = MyFilter.qs
    context = {
        'job': job,
        'MyFilter': MyFilter,
    }
    return render(request,'superadmin/job_pending_list.html',context)

@login_required()
def job_published(request,pk):
    person = get_object_or_404(Job, pk=pk)
    person.is_published = True
    person.save()
    return redirect('job_pending_list')

@login_required()
def worker_pending_list(request):
    worker = User.objects.all().filter(is_worker = True)
    MyFilter = ActiveFilter(request.GET, queryset=worker)
    worker = MyFilter.qs
    context = {
        'worker': worker,
        'MyFilter': MyFilter,
    }
    return render(request,'superadmin/worker_pending_list.html',context)

@login_required()
def worker_active_account(request,pk):
    person = get_object_or_404(User, pk=pk)
    person.is_active = True
    person.save()
    return redirect('worker_pending_list')

@login_required()
def client_pending_list(request):
    customer = User.objects.all().filter(is_customer = True)
    MyFilter = ActiveFilter(request.GET, queryset=customer)
    customer = MyFilter.qs
    context = {
        'customer': customer,
        'MyFilter': MyFilter,
    }
    return render(request,'superadmin/customer_pending_list.html',context)

@login_required()
def client_active_account(request,pk):
    person = get_object_or_404(User, pk=pk)
    person.is_active = True
    person.save()
    return redirect('client_pending_list')

@login_required()
def superadminprofile(request):
    return render(request, 'superadmin/SuperAdminProfile.html')


# Super Admin Profile Create
@login_required()
def SuperAdminProfileCreateView(request):
    form = SuperAdminProfileUpdateForm()
    if request.method == 'POST':
        form = SuperAdminProfileUpdateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('superadminprofile')
    return render(request, 'superadmin/super_admin_profile_create.html', {'form': form})


# Super Admin profile Update
@login_required()
def SuperAdminProfileUpdateView(request, pk):
    person = get_object_or_404(Profile, pk=pk)
    form = SuperAdminProfileUpdateForm(instance=person)
    if request.method == 'POST':
        form = SuperAdminProfileUpdateForm(request.POST,request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('superadminprofile')
    return render(request, 'superadmin/super_admin_profile_create.html', {'form': form})


# Super Admin User Profile Update
@login_required()
def SuperAdminUpdateView(request, pk):
    person = get_object_or_404(User, pk=pk)
    u_form = SuperAdminSignUpUpdateForm(instance=person)
    if request.method == 'POST':
        u_form = SuperAdminSignUpUpdateForm(request.POST, instance=person)
        if u_form.is_valid():
            u_form.save()
            return redirect('superadminprofile')
    return render(request, 'superadmin/superadmin_reg.html', {'u_form': u_form})


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'superadmin/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('login')

@login_required()
def list_category(request):
    category = Country.objects.all()
    return render(request,'superadmin/super_admin_category_list.html',{'category': category})

@login_required()
def create_category(request):
    form = SuperAdminCategoryForm()
    if request.method == 'POST':
        form = SuperAdminCategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    return render(request, 'superadmin/super_admin_category_create.html', {'form': form})

@login_required()
def update_category(request, pk):
    category = get_object_or_404(Country, pk=pk)
    form = SuperAdminCategoryForm(instance=category)
    if request.method == 'POST':
        form = SuperAdminCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    return render(request, 'superadmin/super_admin_category_update.html', {'form': form})


class delete_category(DeleteView):
    model = Country
    template_name = 'superadmin/super_admin_category_delete.html'
    success_url = 'http://127.0.0.1:8000/superadmin/super/admin/category/list/'


def SubCategoryView(request):
    subcategory = City.objects.all()
    MyFilter = CategoryFilter(request.GET, queryset=subcategory)
    subcategory = MyFilter.qs
    context = {
        'subcategory': subcategory,
        'MyFilter': MyFilter,
    }
    return render(request, 'superadmin/super_admin_sub_category_list.html', context)


class SubCategoryCreate(CreateView):
    model = City
    template_name = 'superadmin/super_admin_sub_category_create.html'
    form_class = SuperAdminSubCategoryForm
    success_url = 'http://127.0.0.1:8000/superadmin/super/admin/sub/category/list/'


class SubCategoryUpdate(UpdateView):
    model = City
    form_class = SuperAdminSubCategoryForm
    template_name = 'superadmin/super_admin_sub_category_update.html'
    success_url = 'http://127.0.0.1:8000/superadmin/super/admin/sub/category/list/'


class SubCategoryDelete(DeleteView):
    model = City
    template_name = 'superadmin/super_admin_sub_category_delete.html'
    success_url = 'http://127.0.0.1:8000/superadmin/super/admin/sub/category/list/'