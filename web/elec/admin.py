from django.contrib import admin
# Register your models here.
from .models import AccountInfo, Posts, News

admin.site.register(AccountInfo)
admin.site.register(Posts)
admin.site.register(News)
