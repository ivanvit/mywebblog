from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'superblog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pubdate')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class vote(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'