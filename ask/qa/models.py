# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class QuestionManager(models.Manager): # менеджер модели Question
    def prog_load(self, since, limit=2):
        qs = self.order_by('-id')
        res = list()
        if since is not None:
            qs = qs.filter(id__lt=since)
        for q in qs[:100]:
            res.append(q)
            if len(res) >= limit:
                break
        return res

    def new(self): # метод возвращающий последние добавленные вопросы
        return self.order_by('-added_at', '-pk')

    def popular(self): # метод возвращающий вопросы отсортированные по рейтингу
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255) #заголовок вопроса
    text = models.TextField() #полный текст вопроса
    added_at = models.DateField(auto_now_add=True) # дата добавления вопроса
    rating = models.IntegerField(default=0) # рейтинг вопроса (число)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # автор вопроса
    likes = models.ManyToManyField(User, related_name='likes_user') # список пользователей, поставивших "лайк"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('question', kwargs={'q_id': self.pk})
        
class Answer(models.Model): # ответ
    text = models.TextField() # текст ответа
    added_at = models.DateField(auto_now_add=True) # дата добавления ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # вопрос, к которому относится ответ
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) # автор ответа

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("-added_at",)