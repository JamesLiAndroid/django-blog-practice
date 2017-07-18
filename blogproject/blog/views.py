from django.shortcuts import render, get_object_or_404

# Create your views here.
# from markdown import *

import markdown
from .models import Post, Category


def index(request):
    """
    -created_time
    post_list = Post.objects.all().order_by('-created_time') #
    """
    post_list = Post.objects.all().order_by('-create_time') # '-'表示逆序！不加代表正序！
    return render(request, 'blog/index.html', context = {'post_list': post_list})

def detail(request, pk):
    print('pk=', pk)
    post = get_object_or_404(Post, pk = pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
        ])
    return render(request, 'blog/detail.html', context={'post':post})

def archives(request, year, month):
    print(year, month)
    post_list = Post.objects.filter(create_time__year=year,
            create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list' : post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
