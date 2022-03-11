from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()  # not null
    modify_date = models.DateTimeField(null=True, blank=True)  # null 허용 blank 폼테이터 null
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천수 - 다대다 관계

    def __str__(self):      # 데이터 조회시 id가 아니라 실제 제목을 보여줌
        return self.subject

class Answer(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content    # 데이터 조회시 실제 내용을 보여줌



