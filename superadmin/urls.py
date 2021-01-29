from django.urls import path

from superadmin import views

urlpatterns = [
    path('super/admin/profile/create/', views.SuperAdminProfileCreateView, name='superadminprofilecreate'),
    path('super/admin/profile/view/', views.superadminprofile, name='superadminprofile'),
    path('super/admin/profile/update/<int:pk>/', views.SuperAdminUpdateView, name='superadminprofileupdate'),
    path('superadmin/profile/update/<int:pk>/', views.SuperAdminProfileUpdateView, name='superadminprofilecreateupdate'),
    path('superadmin/change/password/', views.ChangePasswordView.as_view(), name='super_admin_change_password'),

    path('super/admin/worker/pending/list/',views.worker_pending_list,name='worker_pending_list'),
    path('super/admin/worker/active/<int:pk>/',views.worker_active_account,name='worker_active_account'),

    path('super/admin/client/pending/list/',views.client_pending_list,name='client_pending_list'),
    path('super/admin/client/active/<int:pk>/',views.client_active_account,name='client_active_account'),

    path('super/admin/job/pending/list/',views.job_pending_list,name='job_pending_list'),
    path('super/admin/job/published/<int:pk>/',views.job_published,name='job_published'),


    path('super/admin/category/list/',views.list_category,name='list_category'),
    path('super/admin/category/create/',views.create_category,name='create_category'),
    path('super/admin/category/update/<int:pk>/', views.update_category, name='update_category'),
    path('super/admin/category/delete/<int:pk>/', views.delete_category.as_view(), name='delete_category'),

    path('super/admin/sub/category/list/',views.SubCategoryView,name='list_subcategory'),
    path('super/admin/sub/category/create/',views.SubCategoryCreate.as_view(),name='create_subcategory'),
    path('super/admin/sub/category/update/<int:pk>/', views.SubCategoryUpdate.as_view(), name='update_subcategory'),
    path('super/admin/sub/category/delete/<int:pk>/', views.SubCategoryDelete.as_view(), name='delete_subcategory'),


]