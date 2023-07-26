from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.views import signup, dashboard, add_lead, leads_list, leads_detail, delete_leads,edit_leads

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('log-in/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/leads/add-lead/', add_lead, name='add_lead'),
    path('dashboard/leads/lead-list/', leads_list, name='leads_list'),
    path('dashboard/leads/<int:pk>/', leads_detail, name='leads_detail'),
    path('dashboard/leads/<int:pk>/delete/', delete_leads, name='leads_delete'),
    path('dashboard/leads/<int:pk>/edit/', edit_leads, name='leads_edit'),
]
