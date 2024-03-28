from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Endereço de e-mail'), unique=True)
    full_name = models.CharField(_('Nome'), max_length=75, null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    picture = models.CharField(_('Imagem Google'), max_length=250, null=True, blank=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        db_table = 'users'

    def __str__(self):
        return self.email