# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Comment,Post


def post_list(request):
    posts = Post.object.all()
    context = {
        'posts' : posts
    }

    return render(request,"post/post.html",context)
# Create your views here.
