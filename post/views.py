# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Comment,Post
from member.models import User


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }

    return render(request,"post.html",context)
# Create your views here.
