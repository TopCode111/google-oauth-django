# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('calendar', views.calendar, name='calendar'),
    path('google_oauth/redirect/', views.RedirectOauthView, name='google_auth'),
    path('google_oauth/callback/', views.CallbackView),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
