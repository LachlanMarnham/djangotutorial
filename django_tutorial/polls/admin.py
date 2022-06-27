from django.contrib import admin
from django_tutorial.polls.models import Question, Choice


admin.site.register(Question)
admin.site.register(Choice)
