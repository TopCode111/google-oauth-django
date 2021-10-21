import google_apis_oauth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle
import os
import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.db import connection
from django.db.models import F
#from .models import CalendarEvents, CalendarRemindersChange, CalendarAttendees


if os.getcwd() == '/Users/xxxx':
    JSON_FILEPATH = '/Users/xxxx/.credentials/credentials.json'

else:
    JSON_FILEPATH = '/app/google-credentials.json'
    REDIRECT_URI = 'https://biz-dashboard-21-test.herokuapp.com/google_oauth/callback/'
    HOME = 'https://biz-dashboard-21-test.herokuapp.com/'

SCOPES = ['https://www.googleapis.com/auth/calendar']
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

connection.autocommit = True

def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)


def CallbackView(request):
    credentials = google_apis_oauth.get_crendentials_from_callback(request, JSON_FILEPATH, SCOPES, REDIRECT_URI)

    # Stringify credentials for storing them in the DB
    stringified_token = google_apis_oauth.stringify_credentials(credentials)

    filename = 'token_' + request.user.username + '.pickle'

    with open(filename, 'wb') as token:
        pickle.dump(stringified_token, token)

    # Store the credentials safely in the DB
    return HttpResponseRedirect(HOME)


def get_events_server(request):
    filename = 'token_' + request.user.username + '.pickle'
    print(filename)

    with open(filename, 'rb') as token:
        stringified_token = pickle.load(token)

    creds, refreshed = google_apis_oauth.load_credentials(stringified_token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def get_events_local(request):
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(JSON_FILEPATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def get_calendar_data(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    next_week = (datetime.datetime.utcnow() + datetime.timedelta(days=7)).isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary',
                                          timeMin=now,
                                          timeMax=next_week,
                                          singleEvents=True,
                                          timeZone='GMT+9:00',
                                          orderBy='startTime').execute()

    return events_result.get('items', [])