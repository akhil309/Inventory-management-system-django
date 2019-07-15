from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')



    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs= {'pk': self.pk})


    def __str__(self):
        return self.user.username