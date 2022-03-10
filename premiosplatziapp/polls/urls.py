
from django.urls import path

from . import views

app_name="polls/"
urlpatterns=[
    #ex: /polls/5/
    path("",views.IndexView.as_view(), name="index"),
    #ex: /polls/5/
    path("<int:pk>/",views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/results
    path("<int:pk>/results/",views.ResuldView.as_view(), name="results"),
    #ex: /polls/5/votes
    path("<int:question_id>/votes/",views.votes, name="votes"),
]