from django.contrib import admin

# Register your models here.

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']

admin.site.register(Post, PostAdmin) # 将新增的PostAdmin添加进来！
admin.site.register(Category)
admin.site.register(Tag)
