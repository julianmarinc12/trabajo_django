
from django.utils import timezone
from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


#def index(request):
 #   lastest_question_list = Question.objects.all()
  #  return render(request,"polls/index.html",{
   #     "lastest_question_list" : lastest_question_list
    #})



#def detail(request, question_id):
 #   question=get_object_or_404(Question, pk=question_id)
  #  return render(request,"polls/detail.html",{
   #     "question":question
    #})


#def results(request, question_id):
 #   question = get_object_or_404(Question, pk= question_id)
  #  return render(request,"polls/results.html",{
   #     "question":question
    #})
    
class IndexView(generic.ListView):
    
    template_name ="polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name ="polls/detail.html"

    def get_queryset(self) :
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResuldView(generic.DetailView):
    model = Question
    template_name ="polls/results.html"

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
            "question" : question,
            "error_message": "no eegiste una respuesta"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))