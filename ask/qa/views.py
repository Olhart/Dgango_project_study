from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage

from qa.models import *
from qa.forms import *

def pagination(request, qs):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    try:
        limit = int(request.GET.get('limit', 10))
        if limit > 10:
            limit = 10
    except ValueError:
        limit = 10
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator
    
def main(request):
    qs_questions = Question.objects.new()
    page, paginator = pagination(request, qs_questions)
    context = {
        'page': page,
        'paginator': paginator,
        'addr': 'home'
    }
    return render(request, 'qa/pagination.html', context)

def pop_questions(request):
    qs_questions = Question.objects.popular()
    page, paginator = pagination(request, qs_questions)
    context = {
        'page': page,
        'paginator': paginator,
        'addr': 'at_pop'
    }
    return render(request, 'qa/pagination.html', context)

def question(request, **kwargs):
    try:
        q = Question.objects.get(pk=kwargs['q_id'])
    except (ObjectDoesNotExist, ValueError):
        raise Http404
    answers = Answer.objects.filter(question=q)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save() #q)
            url = q.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': kwargs['q_id']})
    context = {
        'question': q,
        'answers': answers,
        'form': form
    }
    return render(request, 'qa/question.html', context)

def new_questions(request):
    since = request.GET.get('since')
    questions = Question.objects.prog_load(since=since)
    return render(request, 'qa/base.html', {
        'questions': questions,
        'since': questions[-1].id,
        'home': 'at_new',
    })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST) 
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/form_ask.html', {'form': form})
        
    


def NotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
