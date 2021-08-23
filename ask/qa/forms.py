from django import forms
from qa.models import *

class AskForm(forms.Form):
    title = forms.CharField(max_length=256)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question.objects.create(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        return self.cleaned_data
        
    def save(self): # , q):
        self.cleaned_data['question'] = Question.objects.get(pk=self.cleaned_data['question'])
        answer = Answer.objects.create(**self.cleaned_data)
        #answer.question = q
        answer.save()
        return answer
