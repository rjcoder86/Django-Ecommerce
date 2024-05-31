import re
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=11)
    active = models.BooleanField(default=True) 
    admin = models.BooleanField(default=False)  
    superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name', 'phone']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split(' ')[0].capitalize()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_admin(self):
        return self.superuser
