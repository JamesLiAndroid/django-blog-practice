from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time') # '-'表示逆序！不加代表正序！
    return render(request, 'blog/index.html', context = {
        'post_list': post_list
    })
