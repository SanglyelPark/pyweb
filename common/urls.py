from django.urls import path
from django.contrib.auth import views as auth_views
from common import views

app_name = 'common'

urlpatterns = [
    # LoginView 클래스 - 제네닉 뷰
    # path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('login/', views.login_view, name='login_view'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup, name='signup'),
]