from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AccountInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    location = models.CharField("Location", max_length=100)
    about_me = models.TextField("About Me")

    def __str__(self):
        return self.location
