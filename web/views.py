from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
import json


def index(request):
    # 首页配置
    # return HttpResponse("欢迎访问我的博客首页！")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    })


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
