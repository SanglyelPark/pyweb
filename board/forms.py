from django import forms
from board.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:  # 내부 클래스
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': "제 목",
            'content': "내 용"
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '내용'}