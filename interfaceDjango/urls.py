"""interfaceDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# from django.urls import re_path  # 写正则匹配
from web.views import Login
from web.feeds import AllPostsRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login),
    path('', include('web.urls')),
    path('', include('comments.urls')),

    # 记得在顶部引入 AllPostsRssFeed
    path('all/rss/', AllPostsRssFeed(), name='rss'),

    # 其它...
    path('search/', include('haystack.urls')),
]
