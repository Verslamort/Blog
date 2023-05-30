from django.http import Http404
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm, BlogForm
from django.contrib.auth.decorators import login_required


def index(request):
    """主页"""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_blog(request):
    """添加新博客"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    """编辑博客"""
    blogpost = BlogPost.objects.get(id=blog_id)
    title = blogpost.title

    check_topic_owner(blogpost, request)
    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'blogpost': blogpost, 'title': title, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)


def check_topic_owner(blogpost, request):
    if blogpost.owner != request.user:
        raise Http404
