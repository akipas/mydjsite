# Create your views here.
from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    if question_id > 10:
        raise Http404
    return HttpResponse("You are looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)

def date_actuelle(request):
    return render(request, 'polls/date.html', {'date':datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    return render(request,'polls/addition.html', locals())
