from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.workerprofileviewhome, name='worker_base'),
    path('job/<int:pk>/', views.JobPostView, name='job_base_apply'),
    path('worker/profile/<int:pk>/', views.SingleProfile, name='worker_list'),
    path('job/post/details/<int:pk>/', views.JobSingleDetails, name='job_list_details'),
    path('job/', views.JobView, name='job_base'),
    path('job/applied/', views.Applied_Job_View, name='apply_job_view'),

    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),

    # worker
    path('profile/', views.workerprofile, name='profile'),
    path('worker/registration/', views.WorkerCreateView, name='person_add'),
    path('worker/registration/update/<int:pk>/', views.WorkerUpdateView, name='person_change'),

    path('Worker/service/add/', views.PersonCreateView, name='service_add'),
    path('Worker/service/<int:pk>/update', views.PersonUpdateView, name='service_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    path('worker/change/password/', views.ChangePasswordView.as_view(), name='worker_change_password'),
    # path('password-change/',
    #      auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
    #      name='password_change'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(
    #          template_name='accounts/password_change_done.html'),
    #      name='password_change_done'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/log_in.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
