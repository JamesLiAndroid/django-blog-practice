from django.shortcuts import render, get_object_or_404

# Create your views here.
# from markdown import *

import markdown
from .models import Post, Category
from comments.forms import CommentForm

# 把 index 视图函数改造成类视图函数。
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
# 改造完毕

# 原始的index
def index(request):
    """
    -created_time
    post_list = Post.objects.all().order_by('-created_time') #
    """
    post_list = Post.objects.all().order_by('-create_time') # '-'表示逆序！不加代表正序！
    return render(request, 'blog/index.html', context = {'post_list': post_list})

# 改造Detail视图
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        reponse = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量+1
        self.object.increase_views()

        # 视图必须返回一个HttpResponse
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form' : form,
            'comment_list' : comment_list
        })
        return context


def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    # 文章阅读量+1
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

# 对archives进行改造
class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        # archs = get_object_or_404(Post, create_time__year=self.kwargs.get('year'), create_time__month=self.kwargs.get('month'))
        return super(ArchivesView, self).get_queryset().filter(create_time__year = year, create_time__month=month)


def archives(request, year, month):
    print(year, month)
    post_list = Post.objects.filter(create_time__year=year,
            create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list' : post_list})

# 对category进行改造, 可以继承自IndexView
class CategoryView(IndexView):
#    model = Post
#    template_name = 'blog/index.html'
#    context_object_name = 'post_list'
    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk')) # self.kwargs.get('pk') 来获取从 URL 捕获的分类 id 值。
        return super(CategoryView, self).get_queryset().filter(category=cate)

# category改造结束

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
