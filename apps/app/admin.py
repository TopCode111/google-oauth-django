from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#from .models import Profile, Issue, Decision, UserAuth, CalendarEvents, CalendarRemindersChange
from .models import UserAuth
admin.site.site_title = 'ダッシュボード管理画面'
admin.site.site_header = 'ダッシュボード管理画面'
admin.site.index_title = 'メニュー'

# class ProfileResource(resources.ModelResource):
#     # Modelに対するdjango-import-exportの設定
#     class Meta:
#         model = Profile

# @admin.register(Profile)
# class ProfileAdmin(ImportExportModelAdmin):
#     # ImportExportModelAdminを利用するようにする
#     ordering = ['id']
#     list_display = ('id', 'firstname', 'lastname', 'role', 'profile_pic', 'strengths', 'developments', 'lifestyle_needs')
#     list_editable = ('firstname', 'lastname', 'role', 'profile_pic', 'strengths', 'developments', 'lifestyle_needs')
#     list_filter = ('firstname', 'lastname', 'role')

class UserAuthResource(resources.ModelResource):
    class Meta:
        model = UserAuth

@admin.register(UserAuth)
class UserAuthAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'username', 'firstname_jp', 'lastname_jp', 'google_oauth_token')
    list_editable = ('username', 'firstname_jp', 'lastname_jp', 'google_oauth_token')

# class DecisionResource(resources.ModelResource):
#     # Modelに対するdjango-import-exportの設定
#     class Meta:
#         model = Decision

# @admin.register(Decision)
# class DecisionAdmin(ImportExportModelAdmin):
#     # ImportExportModelAdminを利用するようにする
#     ordering = ['id']
#     list_display = ('id', 'profile', 'message', 'detail', 'response', 'response_detail',)
#     list_editable = ('profile', 'message', 'detail')
#     list_filter = ('profile',)

# class IssueResource(resources.ModelResource):
#     # Modelに対するdjango-import-exportの設定
#     class Meta:
#         model = Issue

# @admin.register(Issue)
# class IssueAdmin(ImportExportModelAdmin):
#     # ImportExportModelAdminを利用するようにする
#     ordering = ['id']
#     list_display = ('id', 'profile', 'issue', 'detail', 'response')
#     list_editable = ('profile', 'issue', 'detail')
#     list_filter = ('profile',)


# @admin.register(CalendarEvents)
# class CalEventsAdmin(ImportExportModelAdmin):
#     # ImportExportModelAdminを利用するようにする
#     list_display = ('username', 'user_email', 'event_name', 'event_name_prev',
#                     'event_sdate', 'event_sdate_prev',
#                     'event_stime', 'event_stime_prev',
#                     'event_edate', 'event_edate_prev',
#                     'event_etime', 'event_etime_prev',
#                     'event_attendee', 'event_attendee_prev',
#                     'event_location', 'event_location_prev',
#                     'existing_flg', 'existing_flg_prev', 'new_flg',
#                     'change_sdate_flg', 'change_edate_flg', 'change_location_flg',
#                     'zoom_flg', 'location_missing_flg'
#                     )


# @admin.register(CalendarRemindersChange)
# class CalendarRemindersChangeAdmin(ImportExportModelAdmin):
#     # ImportExportModelAdminを利用するようにする
#     list_display = ('username', 'user_email', 'event_name', 'event_name_prev',
#                     'event_sdate', 'event_sdate_prev',
#                     'event_stime', 'event_stime_prev',
#                     'event_edate', 'event_edate_prev',
#                     'event_etime', 'event_etime_prev',
#                     'event_location', 'event_location_prev',
#                     'change_sdate_flg', 'change_edate_flg', 'change_location_flg',
#                     'existing_flg', 'existing_flg_prev', 'new_flg')

