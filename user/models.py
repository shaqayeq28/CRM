from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
from utils.base_model import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, related_name='user', on_delete=models.PROTECT, verbose_name=_('user'))
