from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from utils.base_model import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, related_name='user', on_delete=models.PROTECT, verbose_name=_('user'))


class Lead(BaseModel):
    LOW = 'LOWW'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICES = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    STATUS_CHOICES = (
        (NEW, 'new'),
        (CONTACTED, 'contacted'),
        (WON, 'won'),
        (LOST, 'LOST'),
    )

    name = models.CharField(verbose_name=_('name'), max_length=255)
    email = models.EmailField(verbose_name=_('email'))
    created_by = models.ForeignKey(User, verbose_name='created by', related_name='leads', on_delete=models.PROTECT)
    priority = models.CharField(verbose_name=_('priority'), max_length=150, choices=PRIORITY_CHOICES, default=MEDIUM)
    status = models.CharField(verbose_name=_('status'), max_length=150, choices=STATUS_CHOICES, default=NEW)
    description = models.TextField(verbose_name=_('description'), blank=True)

    def __str__(self):
        return f'{self.name} - {self.priority}'
