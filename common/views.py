from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from templates.common.forms import UserForm

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None: # 일치한다면
            login(request, user)  # 접속이 됨(로그인 됨)
            return redirect('board:index')
        else:
            error = "아이디나 비밀번호가 일치하지 않습니다."
            return render(request, 'common/login.html', {'error': error})

    else:
        return render(request, 'common/login.html')

def logout_view(request):
    #로그 안웃 - 힘수형 view(FBV)
    logout(request)
    return redirect('board:index')

def signup(request, ):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():      # 유효성 검사
            form.save()              # db 저장

            # 회원 가입후 자동 로그인
            username = form.cleaned_data.get('username')   # 사용자 ID
            password1 = form.cleaned_data.get('password1')  # 비밀번호
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('board:index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)
