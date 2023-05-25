from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm, BlogForm


def index(request):
    """主页"""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)


def new_blog(request):
    """添加新博客"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def edit_blog(request, blog_id):
    """编辑博客"""
    blogpost = BlogPost.objects.get(id=blog_id)
    title = blogpost.title

    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'blogpost': blogpost, 'title': title, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
