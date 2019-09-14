from django.shortcuts import render_to_response
from django.http.response import HttpResponse
import json


# Create your views here.
def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['username'] = username
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result, content_type="application/json;charset=utf-8")
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
