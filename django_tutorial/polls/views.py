from django.http import HttpResponse


def index(request):
    return HttpResponse("<ul><li>Hello, world. You're at the polls index.</li></ul>")
