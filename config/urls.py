"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include 함수를 포함하고
from board import views     # 초기화면 연결 설정

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),     # 127.0.0.1:8000 초기화면 연결 설정
    path('board/', include('board.urls')),  # 127.0.0.1:8000/board/  # board앱의 url를 포함시킴
    path('common/', include('common.urls')),  # 127.0.0.1:8000/common/
    path('poll/', include('poll.urls')),  # 127.0.0.1/poll/
    path('book/', include('book.urls')),
]
