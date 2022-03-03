from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from board.models import Question
from board.forms import QuestionForm

def index(request):
    question_list = Question.objects.order_by('-create_date') # '-' 내림 차순정렬
    # question_list = Question.objects.all()
    # return HttpResponse("<h2>Hello~ Django!!</h2>")
    return render(request, 'board/question_list.html',
                  {'question_list': question_list})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'board/detail.html', {'question': question})

def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST) # 내용이 작성된 폼
        if form.is_valid():
            question = form.save(commit=False)  # 가저장
            question.create_date = timezone.now()
            question.save() # 실제 저장
            return redirect('board:index')
    else:      #request.method == "GET"
        form = QuestionForm()  # 질문 등록 폼 객체 변수 생성
    return render(request, 'board/question_form.html', {'form': form})
