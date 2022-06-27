from django.http import HttpResponse
from django_tutorial.polls.models import Question
from django.shortcuts import render


def index(request):
    latest_questions_query_set = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_questions_query_set,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You\'re looking at the results of question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')
