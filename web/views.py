from django.shortcuts import render_to_response, get_object_or_404, render
from django.http.response import HttpResponse
# from django.http import HttpResponse
# 引入 Post Category Tag 类
from .models import Post, Category, Tag
import json, markdown, re
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify


def index(request):
    # 首页配置
    # return HttpResponse("欢迎访问我的博客首页！")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    })


#   编写 detail 视图函数
def detail(request, pk):
    # 判断pk存在于数据库,真post;否404
    post = get_object_or_404(Post, pk=pk)
    # 实例md 的convert 方法将 post.body 中的 Markdown 文本解析成 HTML文本

    # 阅读量 +1
    post.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])

    # 指定 body 为markdown文本内容
    post.body = md.convert(post.body)

    # 处理空目录, 用正则筛选
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


# 编写 archive 视图函数
def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 编写 category 视图函数
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 编写 tag 视图函数
def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['username'] = username
        result['password'] = password
        results = json.dumps(result)
        return HttpResponse(results, content_type="application/json;charset=utf-8")
    else:
        return render_to_response('login.html')


'''
def Login(request):
    if request.method == 'GET':
        result = {}
        username = request.GET.get('username')
        mobile = request.GET.get('mobile')
        data = request.GET.get('data')
        result['username'] = username
        result['mobile'] = mobile
        result['data'] = data
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')
'''
