from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm
from django.contrib import messages

def index(request):
    #인덱스 페이지
    question_list = Question.objects.order_by('-pk')[:3]
    context = {'question_list': question_list}
    return render(request, 'board/index.html', context)

def boardlist(request):
    #질문 목록
    question_list = Question.objects.order_by('-create_date')  #'-'내림 차순, -pk도 가능
    # question_list = Question.objects.all()  #db에서 전체 검색
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    # 검색 처리
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |     # 제목 검색(밑줄 2개임)
            Q(content__icontains=kw) |      # 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이
            Q(answer__author__username__icontains=kw) |  # 답변 글쓴이
            Q(answer__content__icontains=kw) |  # 질문 글쓴이
            Q(comment__content__icontains=kw)
        ).distinct()

    # 페이지 처리
    paginator = Paginator(question_list, 10)    #페이지당 10개 자료
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'board/question_list.html', context)
    # return HttpResponse("<h2>Hello~ Django!!</h2>")

def detail(request, question_id):
    #상세 페이지
    question = get_object_or_404(Question, pk=question_id)  #url경로 오류 처리
    #question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)