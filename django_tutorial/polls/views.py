from django.http import HttpResponse


def index(request):
    return HttpResponse("<ul><li>Hello, world. You're at the polls index.</li></ul>")


def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You\'re looking at the results of question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')
