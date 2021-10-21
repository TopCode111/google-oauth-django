from django.db import models
from django import forms
from django.contrib.auth.models import User


class UserAuth(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE, blank=True, null=True)
    firstname_jp = models.CharField(max_length = 100, blank=True, null=True)
    lastname_jp = models.CharField(max_length=100, blank=True, null=True)
    google_oauth_token = models.CharField(max_length=256, blank=True, null=True)
