from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader

from .models import Question, Choice


def main_page(request):
    last_questions = Question.objects.order_by('-date_add')[:7]
    context = {
        'last_questions': last_questions
    }

    return render(request, 'polls/main_page.html', context)


def question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question
        }
    except Question.DoesNotExist:
        raise Http404(" Question not exist")

    return render(request, 'polls/question_detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }

    return render(request, 'polls/results.html', context)


def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You forgot to select a choice"
        }
        return render(request, 'polls/question_detail.html', context)

    else:
        select.votes += 1
        select.save()

        return HttpResponseRedirect(reverse('results', args=(question_id,)))


def results_data(request, obj_id):
    vote_data = []

    question = Question.objects.get(pk=obj_id)
    votes = question.choice_set.all()

    for vote in votes:
        vote_data.append({vote.choice_text: vote.votes})

    return JsonResponse(vote_data, safe=False)
