from django.shortcuts import render, get_object_or_404

# Create your views here.
# from markdown import *

import markdown
from .models import Post, Category
from comments.forms import CommentForm

def index(request):
    """
    -created_time
    post_list = Post.objects.all().order_by('-created_time') #
    """
    post_list = Post.objects.all().order_by('-create_time') # '-'表示逆序！不加代表正序！
    return render(request, 'blog/index.html', context = {'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    # 阅读量+1
    post.increase_views()

    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
        ])
    # Form表单操作
    form = CommentForm()
    # 获取Post下面的全部评论
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    print(year, month)
    post_list = Post.objects.filter(create_time__year=year,
            create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list' : post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
