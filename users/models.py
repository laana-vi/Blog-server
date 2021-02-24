from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class CustomAccountManager(BaseUserManager):

    def create_user(self,  user_name, email, first_name, last_name, date_of_birth, password, **other_fields):

        if not user_name:
            raise ValueError(_('You must provide a username'))

        if not email:
            raise ValueError(_('You must provide an email address'))

        if not first_name:
            raise ValueError(_('You must provide a first name'))

        if not last_name:
            raise ValueError(_('You must provide a last name'))

        if not date_of_birth:
            raise ValueError(_('You must provide a date of birth'))

        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email, first_name=first_name,
                          last_name=last_name, date_of_birth=date_of_birth, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,  user_name, email, first_name, last_name, date_of_birth, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(user_name, email, first_name, last_name, date_of_birth, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    userobjects = models.Manager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'date_of_birth']

    def __str__(self):
        return self.user_name


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for A Geeks View Blog",
        # message:
        "Please copy and paste token into your browser. Token: "+ reset_password_token.key,
        # from:
        "ageeksviewblog@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
