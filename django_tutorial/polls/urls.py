from django.urls import path


from django_tutorial.polls import views


urlpatterns = [
    path('', views.index, name='index'),
]
