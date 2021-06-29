from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


from .models import *
def index(request):

    all_questions = list(Question.objects.all())
    all_classes = list(Class.objects.all())

    context = {
        'all_questions': all_questions,
        'all_classes': all_classes
    }
    return render(request, 'index.html', context)

def courses_index(request):

    return render(request, 'courses.html')

def polls_index(request):
    all_questions = list(Question.objects.all())

    context = {
            'all_questions': all_questions,
        }

    return render(request, 'polls.html',context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except ObjectDoesNotExist:
        raise Http404("This question does not exist. Please try again.")

    context = {'question': question}

    return render(request, 'detail.html', context)

def results(request,question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except ObjectDoesNotExist:
        raise Http404("This question does not exist. Please try again.")

    context = {'question': question}

    return render(request, 'results.html',context)

def vote(request, question_id):
    print("question_id",question_id)
    question = get_object_or_404(Question, pk=question_id)
    print("question",question)
    try:
        print("request.POST['choice']",request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("selected_choice",selected_choice)

    except (KeyError, ObjectDoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "Select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('classes:results', args=(question.id,)))