from django.shortcuts import render, redirect

from templates.common.forms import UserForm

def signup(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():      # 유효성 검사
            form.save()              # db 저장
            return redirect('board:index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)
