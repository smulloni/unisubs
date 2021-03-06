# Universal Subtitles, universalsubtitles.org
#
# Copyright (C) 2012 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# http://www.gnu.org/licenses/agpl-3.0.html.

from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from messages.forms import TeamAdminPageMessageForm
from teams.models import (
    Team, TeamMember, TeamVideo, Workflow, Task, Setting, MembershipNarrowing,
    Project, TeamLanguagePreference
)
from videos.models import SubtitleLanguage


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    raw_id_fields = ['user']

class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]
    search_fields = ('name'),
    list_display = ('name', 'membership_policy', 'video_policy', 'is_visible', 'highlight', 'last_notification_time', 'thumbnail')
    list_filter = ('highlight', 'is_visible')
    actions = ['highlight', 'unhighlight', 'send_message']
    raw_id_fields = ['video']

    def thumbnail(self, object):
        return '<img src="%s"/>' % object.logo_thumbnail()
    thumbnail.allow_tags = True

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['message_form'] = TeamAdminPageMessageForm()
        return super(TeamAdmin, self).changelist_view(request, extra_context)

    def send_message(self, request, queryset):
        form = TeamAdminPageMessageForm(request.POST)
        if form.is_valid():
            count = form.send_to_teams(request.POST.getlist(u'_selected_action'), request.user)
            self.message_user(request, _("%(count)s messages sent") % dict(count=count))
        else:
            self.message_user(request, _("Fill all fields please."))
    send_message.short_description = _('Send message')

    def highlight(self, request, queryset):
        queryset.update(highlight=True)
    highlight.short_description = _('Feature teams')

    def unhighlight(self, request, queryset):
        queryset.update(highlight=False)
    unhighlight.short_description = _('Unfeature teams')

class TeamMemberAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'team__name', 'user__first_name', 'user__last_name')
    list_display = ('role', 'team_link', 'user_link')
    raw_id_fields = ('user', 'team')

    def team_link(self, obj):
        url = reverse('admin:teams_team_change', args=[obj.team_id])
        return u'<a href="%s">%s</a>' % (url, obj.team)
    team_link.short_description = _('Team')
    team_link.allow_tags = True

    def user_link(self, obj):
        url = reverse('admin:auth_customuser_change', args=[obj.user_id])
        return u'<a href="%s">%s</a>' % (url, obj.user)
    user_link.short_description = _('User')
    user_link.allow_tags = True

class TeamVideoForm(forms.ModelForm):

    class Meta:
        model = TeamVideo

    def __init__(self, *args, **kwargs):
        super(TeamVideoForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            qs = SubtitleLanguage.objects.filter(video=self.instance.video)
        else:
            qs = SubtitleLanguage.objects.none()

        self.fields['completed_languages'].queryset = qs

class TeamVideoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'team_link', 'created')
    readonly_fields = ('completed_languages',)
    raw_id_fields = ['video', 'team', 'added_by']
    search_fields = ('title', 'video__title')

    def team_link(self, obj):
        url = reverse('admin:teams_team_change', args=[obj.team_id])
        return u'<a href="%s">%s</a>' % (url, obj.team)
    team_link.short_description = _('Team')
    team_link.allow_tags = True

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'team', 'project', 'team_video', 'created')
    list_filter = ('created', 'modified')
    search_fields = ('team__name', 'project__name', 'team_video__title',
                     'team_video__video__title')
    raw_id_fields = ('team', 'team_video', 'project')
    ordering = ('-created',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'team', 'team_video', 'language',
                    'assignee', 'is_complete', 'deleted')
    list_filter = ('type', 'deleted', 'created', 'modified', 'completed')
    search_fields = ('assignee__username', 'team__name', 'assignee__first_name',
                     'assignee__last_name', 'team_video__title',
                     'team_video__video__title')
    raw_id_fields = ('team_video', 'team', 'assignee', 'subtitle_version')
    ordering = ('-created',)

    def is_complete(self, o):
        return True if o.completed else False
    is_complete.boolean = True

class TeamLanguagePreferenceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'team', 'language_code', 'preferred',
                    'allow_reads', 'allow_writes')
    list_filter = ('preferred', 'allow_reads', 'allow_writes')
    search_fields = ('team__name',)
    raw_id_fields = ('team',)

class MembershipNarrowingAdmin(admin.ModelAdmin):
    list_display = ('member', 'team', 'project', 'language')
    list_filter = ('created', 'modified')
    raw_id_fields = ('member', 'project')
    ordering = ('-created',)
    search_fields = ('member__team__name', 'member__user__username')

    def team(self, o):
        return o.member.team
    team.admin_order_field = 'member__team'

class SettingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'team', 'key', 'created', 'modified')
    list_filter = ('key', 'created', 'modified')
    search_fields = ('team__name',)
    raw_id_fields = ('team',)
    ordering = ('-created',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'workflow_enabled')
    list_filter = ('workflow_enabled', 'created', 'modified')
    search_fields = ('team__name', 'name')
    raw_id_fields = ('team',)
    ordering = ('-created',)


admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamVideo, TeamVideoAdmin)
admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TeamLanguagePreference, TeamLanguagePreferenceAdmin)
admin.site.register(MembershipNarrowing, MembershipNarrowingAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Project, ProjectAdmin)
