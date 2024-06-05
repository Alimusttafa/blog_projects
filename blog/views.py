from django.shortcuts import render
from .models import Post
from django.http import Http404

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list_posts.html', {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/post/detail.html', {'post': post})
    