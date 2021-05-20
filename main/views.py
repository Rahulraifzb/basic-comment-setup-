from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Post, Comment

from django.views.generic import DetailView

from django.urls import reverse

from main.filter import extra
# Create your views here.


def postList(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post.html', context)


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.filter(parent=None)
    replies = post.comment_set.filter().exclude(parent=None)

    replyDict = {}
    for reply in replies:
        if reply.parent.id in replyDict:
            replyDict[reply.parent.id].append(reply)
        else:
            replyDict[reply.parent.id] = [reply]

    context = {
        'post': post,
        'comments': comments,
        'replies': replyDict,
    }
    return render(request, 'post_detail.html', context)


def postComment(request, pk):
    if request.method == "POST":
        user = request.user
        post = Post.objects.get(id=pk)
        comment = request.POST.get('comment')
        parentid = request.POST.get('parentid')

        if parentid:
            parentComment = Comment.objects.get(id=parentid)
            postcomment = Comment(user=user, post=post,
                                  comment=comment, parent=parentComment)
            postcomment.save()
        else:
            postcomment = Comment(user=user, post=post, comment=comment)
            postcomment.save()

    return redirect(reverse('post-detail', kwargs={'pk': pk}))
