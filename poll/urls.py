from django.urls import path
from . import views

app_name = 'poll'  # 네임 스페이스(소속)

urlpatterns = [
    path('', views.index, name='index'),  # 127.0.0.1/poll/
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/vote/', views.vote, name='vote'),

]