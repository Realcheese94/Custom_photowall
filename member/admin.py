# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#Custom User model을 사용하기위한 절차
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User,UserAdmin)

# Register your models here.
