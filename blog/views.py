from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post
from .forms import PostForm


def post_list(request):
    """
    A view to show all post
    """
    posts = Post.objects.order_by('-created_on')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    A view to show the post details
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    """
    Add a new post to the blog
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post created successfully')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(
                request, 'Failed to add post. Please ensure the form is valid.'
                )
    else:
        form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})


@login_required
def post_edit(request, pk):
    """
    Edit a post in the blog
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(
             request, 'Failed to update post. Please ensure the form is valid.'
                )
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    """ Delete a post from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect('post_list')
