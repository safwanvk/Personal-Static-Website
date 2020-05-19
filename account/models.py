from django.db import models


class Mail(models.Model):
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=250)
