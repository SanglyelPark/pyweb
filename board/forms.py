from django import forms
from board.models import Question, Answer, Comment


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
        labels = {
            'content': '답변내용'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': '댓글'}
