import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.conf import settings
from django.db.models import F
from forms import *
from django.contrib import messages

def dashboard(request):
    return render_to_response('dashboard.html',
                              {'user' : request.user},
                              context_instance=RequestContext(request))

def home(request):
    return dashboard(request)

def feedback(request, qid=None):
    try:
        q = Question.objects.get(pk=qid)
    except:
        messages.error(request, "couldn't find the question you are giving feedback to")
        q = None

    if request.method == 'POST' and q:
        post = request.POST
        post['question'] = q
        form = AddFeedbackForm(post)
        if form.is_valid():
            form.save()
            messages.success(request, "added feedback successfully!")
    else:
        form = AddFeedbackForm()
    return render_to_response('feedback.html',
                              {'form' : form,
                               'q' : q },
                              context_instance=RequestContext(request))

def question(request, qid):
    if request.method == 'GET':
        try:
            q = Question.objects.get(pk=qid)
            if q.user == request.user:
                return render_to_response('question.html',
                                          {'q' : q,
                                           'user' : request.user},
                                          context_instance=RequestContext(request))
            messages.error(request, "you don't own this question")
        except:
            messages.error(request, "couldn't find the question you are looking for")
            q = None
        return home(request)

        
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "added your question!")
            # save it
            pass
    else:
        form = AddQuestionForm()
    return render_to_response('addquestion.html',
                              {'form' : form},
                              context_instance=RequestContext(request))

def question_submit(request):
    pass
