from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class AccountInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    location = models.CharField("Location", max_length=99)
    about_me = models.TextField("About Me")

    def __str__(self):
        return str(self.user)

class Posts(models.Model):
    title = models.CharField("Post title", max_length=119)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Publish Date', default=now)
    pub_edit = models.DateTimeField('Publish Date', auto_now=True)
    post = models.TextField("Post Body")

    def __str__(self):
        return str(self.title)

class News(models.Model):
    title = models.CharField("News title", max_length=20)
    pub_date = models.DateTimeField('Publish Date', default=now)
    post = models.TextField("Post Body", max_length=200)

    def __str__(self):
        return str(self.title)
