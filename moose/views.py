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
                              {'user' : request.user,
                               'hide_toolbar' : True},
                              context_instance=RequestContext(request))


def feedback(request, shortname):
    try:
        q = Question.objects.get(shortname=shortname)
    except Exception as e:
        print e
        try:
            q = Question.objects.get(pk=int(shortname))         # maybe its an id!
        except Exception as e:
            print shortname, e
            messages.error(request, "couldn't find the question you are giving feedback to")
            return HttpResponseRedirect('/')

    if request.method == 'POST' and q:
        # I don't know how to get the sender/message forms to validate, so fuck it.  This is in-house
        post = dict([(k, v[0] if isinstance(v,list) else v) for k, v in request.POST.items()])

        text = post.get('text', '').strip()
        email = post.get('s-email', 'g')
        sender_user = None
        if email:
            try:
                sender_user = User.objects.get(email=email)
                status = 'user'
            except:
                pass
            status = 'email'
        else:
            status = 'anon'

        s = Sender(user=sender_user, email=email, status=status)
        s.save()

        f = Feedback(sender = s, question=q)
        f.save()
        print "text", text
        if text:
            m = Message(feedback=f, text=text)
            m.save()
            messages.success(request, "added feedback successfully!")                
        else:
            messages.error(request, "did not validate form correctly")

    return render_to_response('feedback.html',
                              {'q' : q,
                               'user' : request.user,
                               'hide_toolbar' : True },
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
