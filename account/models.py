from django.contrib.auth import forms
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100),
    email = models.EmailField(max_length=100),
    subject = models.CharField(max_length=100),
    message = models.TextField(max_length=250)
