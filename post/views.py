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
            comment = comment_form.save(commit =False)
            comment.post = post
            comment.author = request.user
            comment.save()
        #post url 을 가진 post_list 뷰로 이동한다.
        return redirect('post:post_list')

def post_detail(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    comment_form = Commentform()
    context={
        'post' : post,
        'comment' : comment_form,
    }
    return render(request,'post_detail.html',context)
