from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
#from .models import Profile, Decision, Issue

import requests
import os

# clickup_team_id = settings.CLICKUP_TEAM
# clickup_list_id = settings.CLICKUP_LIST

# headers = {
#     'Authorization': settings.CLICKUP_TOKEN,
#     'Content-Type': 'application/json'
# }

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['firstname', 'lastname', 'role', 'profile_pic', 'strengths', 'developments', 'lifestyle_needs']

# class DecisionForm(forms.ModelForm):
#     class Meta:
#         model = Decision
#         fields = ['profile', 'message', 'detail']

# class IssueForm(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ['profile', 'issue', 'detail', 'response']
#         widgets = {
#             'response': forms.TextInput(attrs={"placeholder": "コメント内容を入力", "class": "form-control"})
#         }

# class IssueResponseForm(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ['response']
#         widgets = {
#             'response': forms.TextInput(attrs={"placeholder": "コメント内容を入力", "class": "form-control"})
#         }

# class DecisionResponseForm(forms.ModelForm):
#     class Meta:
#         model = Decision
#         fields = ['response_detail']
#         widgets = {
#             'response_detail': forms.TextInput(attrs={"placeholder": "コメント内容を入力", "class": "form-control"})
#         }


# class FindNewsForm(forms.Form):
#     キーワード = forms.CharField(label='', required=False,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "検索ワードを入力"
#                 , "class": "form-control"
#                 , "id":"m-search",
#             }
#         ))

# class CreateTaskForm(forms.Form):
#     タスク名 = forms.CharField(label_suffix='', required = True,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "タスク名を入力",
#                 "class": "form-control"
#             }
#         ))
#     締切日 = forms.DateField(label_suffix='', required = False,
#         widget=forms.DateInput(
#             attrs={
#                 "placeholder": "締切日を入力（YYYY-MM-DD）",
#                 "class": "form-control",
#                 "id": "d_week",
#             }
#         ))
#     担当者 = forms.CharField(label_suffix='', required=False,
#         widget=forms.Select(choices=[('', '----'), (1, 'Elisa Aoki'), (2, 'Ryo Taguchi')],
#             attrs={
#                 "placeholder": "担当者を選択",
#                 "class": "form-control",
#             }
#         ))

    # def __init__(self, *args, **kwargs):
    #     r = requests.get(url="https://api.clickup.com/api/v2/team/" + TEAMID, headers=headers)
    #     users = []
    #     team = r.json()
    #     for team_info in team['team']['members']:
    #         users.append(team_info['user']['username'])
    #     enumerate_users = enumerate(users, 1)
    #
    #     super(CreateTaskForm, self).__init__(*args, **kwargs)
    #     self.fields['担当者'].choices = enumerate_users