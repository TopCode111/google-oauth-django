# -*- encoding: utf-8 -*-

from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.conf import settings
from django.db.models import Sum

#from .get_clickup_tasks import get_clickup_tasks
#from .get_news import get_news
from .get_calendar_events import *

#from .models import Profile, Decision, Issue
#from .forms import IssueForm, CreateTaskForm, IssueResponseForm, DecisionResponseForm

import os
import requests
import datetime


@login_required(login_url="/login/")
def index(request):

    return render(request, 'index.html')


@login_required(login_url="/login/")
def calendar(request):

    if os.getcwd() == '/Users/elisaaoki/biz_dashboard':
        service = get_events_local(request)
    else:
        service = get_events_server(request)

    events = get_calendar_data(service)
    events_list = []

    for event in events:
        events_list.append(event['summary'])

    params = {
        'event_summary': events_list
    }

    return render(request, 'calendar.html', params)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        segment, active_menu = get_segment( request )

        context['segment'] = segment
        context['active_menu'] = active_menu

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

# Helper - Extract current page name from request
def get_segment( request ):
    try:
        segment     = request.path.split('/')[-1]
        active_menu = None

        if segment == '' or segment == 'index.html':
            segment     = 'index'
            active_menu = 'dashboard'

        if segment.startswith('dashboard-'):
            active_menu = 'dashboard'

        return segment, active_menu

    except:
        return 'index', 'dashboard'

