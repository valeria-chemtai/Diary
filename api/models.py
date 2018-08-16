from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True,
                                on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Entry(models.Model):
    title = models.CharField(max_length=60)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Profile, related_name='entries',
                                on_delete=models.CASCADE)


class Content(models.Model):
    text = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    entry_id = models.ForeignKey(Entry, related_name='contents',
                                 on_delete=models.CASCADE)
