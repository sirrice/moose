import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.conf import settings
from django.db.models import F


def home(request):
    return feedback(request)

def feedback(request):
    return render_to_response('feedback.html', {}, context_instance=RequestContext(request))
