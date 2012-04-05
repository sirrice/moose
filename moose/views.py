import random
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.conf import settings
from django.db.models import F
from forms import *
from django.contrib import messages


def home(request):
    if request.user.is_authenticated():
        qform = AddQuestionForm()            
        return render_to_response('dashboard.html',
                                  {'user' : request.user,
                                  'form' : qform},
                                  context_instance=RequestContext(request))
    

    return render_to_response('index.html',
                              {'user' : request.user},
                              context_instance=RequestContext(request))


def feedback(request, shortname):
    try:
        q = Question.objects.get(shortname=shortname)
    except Exception as e:
        print e
        try:
            q = Question.objects.get(pk=int(shortname))         # maybe its an id!
        except Exception as e:
            print e
            messages.error(request, "couldn't find the question you are giving feedback to")
            return HttpResponseRedirect('/')

    if request.method == 'POST' and q:
        post = dict(request.POST)
        post['question'] = q.pk
        print post
        fform = AddFeedbackForm(post, prefix='f')
        sform = AddSenderForm(post, prefix='s')
        mform = AddMessageForm(post, prefix='m')

        if sform.is_valid() and fform.is_valid() and mform.is_valid():
            s = sform.save(commit=False)
            f = fform.save(commit=False)
            m = mform.save(commit=False)
            f.sender = s
            m.feedback = f
            s.save()
            f.save()
            m.save()
            messages.success(request, "added feedback successfully!")
        else:
            messages.error(request, "did not validate form correctly")
    else:
        fform = AddFeedbackForm({'question' : q}, prefix='f')
        sform = AddSenderForm(prefix='s')
        mform = AddMessageForm(prefix='m')
    return render_to_response('feedback.html',
                              {'fform' : fform,
                               'sform' : sform,
                               'mform' : mform,
                               'q' : q,
                               'user' : request.user },
                              context_instance=RequestContext(request))

@login_required
def question(request, qid=None):
    if request.method == 'GET' and qid is not None:
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
            q = form.save(commit=False)
            q.user = request.user
            q.save()
            messages.success(request, "added your question!")
            return redirect('home')
    else:
        form = AddQuestionForm()
    return render_to_response('addquestion.html',
                              {'form' : form},
                              context_instance=RequestContext(request))

def question_submit(request):
    pass
