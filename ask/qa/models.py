from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager): # менеджер модели Question
    def new(self): # метод возвращающий последние добавленные вопросы
        return self.order_by('-added_at')

    def popular(sefl): # метод возвращающий вопросы отсортированные по рейтингу
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255) #заголовок вопроса
    text = models.TextField() #полный текст вопроса
    added_at = models.DateField(auto_now_add=True) # дата добавления вопроса
    rating = models.IntegerField(default=0) # рейтинг вопроса (число)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор вопроса
    likes = models.ManyToManyField(User, related_name='likes_user') # список пользователей, поставивших "лайк"

class Answer(models.Model): # ответ
    text = models.TextField() # текст ответа
    added_at = models.DateField(auto_now_add=True) # дата добавления ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # вопрос, к которому относится ответ
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING) # автор ответа