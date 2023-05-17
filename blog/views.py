from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_on')
    return render(request, 'blog/post_list.html', {'posts': posts})