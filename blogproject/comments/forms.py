#!/usr/bin/env python
# encoding: utf-8

from django import forms
from .models import Comment

# 如果表单对应有一个数据库模型（例如这里的评论表单对应着评论模型），那么使用 ModelForm 类会简单很多，
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text'] # 要展示的数据
