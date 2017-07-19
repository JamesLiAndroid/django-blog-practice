from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from comments.forms import CommentForm

def post_comment(request, post_pk=None):

    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    print("post_pk == ",post_pk)
    post = get_object_or_404(Post, pk=post_pk)

    # Form表单用post请求
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)

            # 将评论和评论的文章关联
            comment.post = post

            # 保存到数据库
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)
        else:
            # Post.objects.filter(category=cate)。这里 post.comment_set.all() 也等价于
            # Comment.objects.filter(post=post)，即根据 post 来过滤该 post 下的全部评论。
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
                }
            return render(request, 'blog/detail.html', context=context)

    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)


