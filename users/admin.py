from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


from django.db import models


admin.site.register(CustomUser)
