from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from user.views import signup,dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('log-in/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
