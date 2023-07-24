from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)
    is_active = models.BooleanField(verbose_name=_('is active'), default=True)

    objects = models.Manager()

    class Meta:
        abstract = True
