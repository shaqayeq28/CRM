from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.views import (signup, dashboard, add_lead, leads_list, leads_detail, delete_leads, edit_leads,
                        convert_lead_to_client, clients_list, clients_detail, add_client, delete_client, edit_clients,
                        my_profile)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('log-in/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/leads/add-lead/', add_lead, name='add_lead'),
    path('dashboard/leads/leads-list/', leads_list, name='leads_list'),
    path('dashboard/leads/<int:pk>/', leads_detail, name='leads_detail'),
    path('dashboard/leads/<int:pk>/delete/', delete_leads, name='leads_delete'),
    path('dashboard/leads/<int:pk>/edit/', edit_leads, name='leads_edit'),
    path('dashboard/leads/<int:pk>/convert/', convert_lead_to_client, name='convert_to_client'),
    path('dashboard/clients/clients-list', clients_list, name='clients_list'),
    path('dashboard/clients/<int:pk>/', clients_detail, name='clients_detail'),
    path('dashboard/clients/add-client/', add_client, name='clients_add'),
    path('dashboard/clients/<int:pk>/delete-client/', delete_client, name='clients_delete'),
    path('dashboard/clients/<int:pk>/add-client/', edit_clients, name='clients_edit'),
    path('dashboard/profile/', my_profile, name='my_profile'),
]
