# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment,Post


admin.site.register(Comment)
admin.site.register(Post)

# Register your models here.
