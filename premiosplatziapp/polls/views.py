from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    lastest_question_list = Question.objects.all()
    return render(request,"polls/index.html",{
        "lastest_question_list" : lastest_question_list
    })



def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html",{
        "question":question
    })


def results(request, question_id):
    return HttpResponse(f"results{question_id}")


def votes(request, question_id):
    return HttpResponse(f"votes{question_id}")