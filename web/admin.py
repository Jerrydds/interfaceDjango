from django.contrib import admin
from .models import Post, Category, Tag
from django.utils import timezone


class PostAdmin(admin.ModelAdmin):
    # 文章列表显示更加详细的信息
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 简化新增文章的表单
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    #  Modeladmin 关联注册的是Post实例保存到数据库, obj.save()
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.modified_time = timezone.now()
        super().save_model(request, obj, form, change)


# 添加注册模型 + Postadmin, 以备调用
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
