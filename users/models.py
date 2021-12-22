from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        """
        Create user by requesting their email address and
        password
        Signup using social accounts will be made easier
        with this
        :param email:
        :param password:
        :param other_fields:
        :return:
        """
        if not email:
            raise ValueError(_('The Email field must be provided'))
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, **other_fields):
        """
        In this section create superuser with email and password
        We use these two fields because it is easier to remember email
        than the django default username
        :param email:
        :param password:
        :param other_fields:
        :return:
        """
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be set to staff=True'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be set to is_superuser=True'))
        return self.create_user(email, password, **other_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(_('Email Address'), max_length=100, unique=True)
    username = models.CharField(max_length=100,
                                blank=True,
                                null=True,
                                unique=False,
                                default='Client-default',
                                )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ClientReview(models.Model):
    subject = models.CharField(max_length=100)
    issue_burning = models.TextField()
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    date_posted = models.DateField()

    def __str__(self):
        return self.subject


class Complaint(models.Model):
    subject = models.CharField(max_length=100)
    complaint = models.TextField()
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    date_posted = models.DateField()

    def __str__(self):
        return self.subject
