from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import BaseModel


class Team(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    members = models.ManyToManyField(User, verbose_name=_('members'), related_name='teams')
    created_by = models.ForeignKey(User, verbose_name=_('created by'), related_name='creators', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
