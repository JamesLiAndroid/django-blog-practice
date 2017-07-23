#!/usr/bin/env python
# encoding: utf-8

# 模板标签的编写！
from django import template
from ..models import Post, Category

from django.db.models.aggregates import Count

register = template.Library()

# 最新文章的模板标签
@register.simple_tag
def get_recent_posts(num = 5):
    return Post.objects.all().order_by('-create_time')[:num]

# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

# Annotate使用
@register.simple_tag
def get_categories():
    # 在顶部引入count函数
    # 两个 model 类通过 ForeignKey 或者 ManyToMany 关联起来，那么就可以使用 annotate 方法来统计数量。
    # Count 计算分类下的文章数，其接收的参数为需要计数的模型的名称
    # 小写的post其实关联的是Post，django这样规定的，不能修改为Post
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


