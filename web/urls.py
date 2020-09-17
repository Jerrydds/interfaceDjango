from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    # 设计文章详情页的 URL
    path('posts/<int:pk>/', views.detail, name='detail'),

]
