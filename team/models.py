from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import Lead, Client
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
    lead = models.ManyToManyField(Lead, verbose_name=_('leads'), related_name='team_leads')
    client = models.ManyToManyField(Client, verbose_name=_('clients'), related_name='team_clients')
    plan = models.ForeignKey(TeamPlan, verbose_name=_('plan'), on_delete=models.PROTECT, related_name='team_plans')
    name = models.CharField(verbose_name=_('name'), max_length=255)
    created_by = models.OneToOneField(User, verbose_name=_('created by'), related_name='creator',
                                      on_delete=models.PROTECT)

    def __str__(self):
        return self.name
