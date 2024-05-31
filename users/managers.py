import re
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, full_name, email, phone, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users Must Have A Email')
        if not full_name:
            raise ValueError('Users Must Have A Full Name')
        if not phone:
            raise ValueError('Users Must Have A Phone Number')
        if not password:
            raise ValueError('Users Must Have A Password')

        if re.fullmatch('^[a-z0-9.]+@[a-z0-9]+.[a-z]{2,}$', email.lower()) is None:
            raise ValueError('Invalid Email Address')

        if re.fullmatch('^[a-z0-9.@#$%^&*-+~!]{8,}$', password.lower()) is None:
            raise ValueError('Password Must Be At Least 8 Characters')

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.full_name = full_name
        user_obj.phone = phone
        user_obj.active = is_active
        user_obj.admin = is_staff
        user_obj.superuser = is_admin
        user_obj.set_password(password)
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, full_name, email, phone, password=None):
        user = self.create_user(
            full_name=full_name, email=email, phone=phone, password=password, is_staff=True)
        return user

    def create_superuser(self, full_name, email, phone, password=None):
        user = self.create_user(full_name=full_name, email=email,
                                phone=phone, password=password, is_staff=True, is_admin=True)
        return user
