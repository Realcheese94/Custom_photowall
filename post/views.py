# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from .models import Comment,Post
from member.models import User
from django.http import HttpResponse
from .forms import Commentform


def post_list(request):
    
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'comments' :comments,
        'posts' : posts,
    }

    return render(request,"post.html",context)

def createcomment(request , post_pk):
    if request.method =='POST':
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST.get('content')
        comment_form = Commentform(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(
                post = post,
                author = request.user,
                content = comment_form.cleaned_data['content']
            )
        #post url 을 가진 post_list 뷰로 이동한다.
        return redirect('post:post_list')
        

