from django.db import models
from django import forms
from django.contrib.auth.models import User


class UserAuth(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True, null=True)
    google_id_token = models.CharField(max_length=2000, blank=True, null=True)
    manual_user = models.BooleanField(default=True)
