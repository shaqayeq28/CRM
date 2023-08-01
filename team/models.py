from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import BaseModel


class TeamPlan(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    price = models.DecimalField(verbose_name=_('price'), max_digits=12, decimal_places=4)
    description = models.TextField(verbose_name=_('description'), blank=True)
    max_leads = models.IntegerField(verbose_name=_('maximum leads'), validators=[MinValueValidator(1)])
    max_clients = models.IntegerField(verbose_name=_('maximum clients'), validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class Team(BaseModel):
    plan = models.ForeignKey(TeamPlan, verbose_name=_('plan'), on_delete=models.PROTECT, related_name='team_plans')
    name = models.CharField(verbose_name=_('name'), max_length=255)
    members = models.ManyToManyField(User, verbose_name=_('members'), related_name='teams')
    created_by = models.ForeignKey(User, verbose_name=_('created by'), related_name='creators',
                                   on_delete=models.PROTECT)

    def __str__(self):
        return self.name
