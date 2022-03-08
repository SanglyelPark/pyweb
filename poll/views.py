from django.http import HttpResponse
from django.shortcuts import render

from poll.models import Question


def index(request):
    question_list = Question.objects.all()
    # return HttpResponse("<h1>안녕~ Django!!</h1>")
    return render(request, 'poll/index.html', {'question_list': question_list})

def detail(request, pk):
    question = Question.objects.get(id=pk)
    return render(request, 'poll/detail.html', {'question': question})

def vote(request, pk):
    #투표하기
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        # 선택 항목 받아 오기
        try:
            choice = request.POST['choice']
        except:
            error = "하나의 항목을 반드시 선택하세요"
            return render(request, 'poll/detail.html',
                          {'question': question, 'error': error})
        choice = request.POST['choice']
        sel_choice = question.choice_set.get(id=choice)
        sel_choice.votes += 1
        sel_choice.save()
        return render(request, 'poll/result.html', {'question': question})
    else:
        return render(request, 'poll/detail.html', id=pk)