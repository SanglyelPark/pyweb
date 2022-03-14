from django.urls import path
from . import views

app_name = 'book'  # 네임 스페이스(소속)

urlpatterns = [
    path('book/', views.django_doc, name='django_doc'),  # 127.0.0.1/poll/
    path('about_me/', views.about_me, name='about_me'),  # 127.0.0.1/poll/
]