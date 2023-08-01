from django.urls import path

from team.views import edit_team

urlpatterns = [
    path('edit/<int:pk>/', edit_team, name='edit_team')
]
