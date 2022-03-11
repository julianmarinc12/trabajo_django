
import datetime

from django.urls.base import reverse
from django.utils import timezone 
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase):


    def test_was_plublished_recently_with_future_questions(self):
        """was_published_recently return false for 
        questions whose pub_date is in the future """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿quien es el mejor cd de platzi?",pub_date=time)
        self.assertIs(future_question.was_plublished_recently(), False)

    def test_was_plublished_recently_with_past_question(self):

        time = timezone.now() - datetime.timedelta(days=30)
        past_questions = Question(question_text="¿quien es el mejor cd de platzi?",pub_date=time)
        self.assertIs(past_questions.was_plublished_recently(), False)

    def test_was_plublished_recently_with_present_question(self):

        time = timezone.now() - datetime.timedelta(days=0)
        present_questions = Question(question_text="¿quien es el mejor cd de platzi?",pub_date=time)
        self.assertIs(present_questions.was_plublished_recently(), True)
    
class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """if no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"no polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])
    
    def test_questions_with_future_pub_date(self):
        """Questions with date greater to timezone.now shouldn't be displayed"""
        time = timezone.now() + datetime.timedelta(seconds=10)
        future_question = Question(question_text = "This is a Question for the test", pub_date = time)
        future_question.save()
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response,"no polls are available")
        self.assertNotIn(future_question, response.context['latest_question_list'])

    def test_questions_with_past_pub_date(self):
        """Questions with date greater to timezone.now shouldn't be displayed"""
        time = timezone.now() - datetime.timedelta(days=10)
        past_question = Question(question_text = "This is a Question for the test", pub_date = time)
        past_question.save()
        response = self.client.get(reverse('polls:index'))
        self.assertIn(past_question, response.context['latest_question_list'])




