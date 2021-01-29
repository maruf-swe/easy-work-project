from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Client import views

urlpatterns = [
    path('Client/Job/Applied/List/', views.Applied_Job_View, name='applied_job_list'),
    path('Client/Job/List/', views.JobView, name='job_list'),
    path('Client/Job/add/', views.JobCreateView, name='job_add'),
    path('Client/Job/<int:pk>/update', views.JobUpdateView, name='job_change'),
    path('Client/Job/delete/<int:pk>/', views.JobDelete.as_view(), name='job_delete'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    path('client/profile/', views.Clientprofile, name='client_profile'),
    path('client/registration/', views.ClientCreateView, name='client_add'),
    path('client/profile/update/<int:pk>/', views.ClientUserUpdateView, name='client_change'),
    path('client/profile/create/', views.ClientProfileCreateView, name='client_profile_create'),
    path('client/profile/<int:pk>/update', views.ClientProfileUpdateView,
         name='client_profile_update'),

    path('client/change/password/', views.ChangePasswordView.as_view(), name='client_change_password'),

]