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

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from videos.models import Video, VIDEO_TYPE_YOUTUBE, Action, SubtitleLanguage, SubtitleVersion,  \
    VideoUrl, AlreadyEditingException
from videos.forms import VideoForm, FeedbackForm, EmailFriendForm, UserTestResultForm, \
    SubtitlesUploadForm, PasteTranscriptionForm, CreateVideoUrlForm, TranscriptionFileForm, \
    AddFromFeedForm
import widget
from django.contrib.sites.models import Site
from django.conf import settings
import simplejson as json
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from widget.views import base_widget_params
from vidscraper.errors import Error as VidscraperError
from auth.models import CustomUser as User
from utils import send_templated_email
from django.contrib.auth import logout
from videos.share_utils import _add_share_panel_context_for_video, _add_share_panel_context_for_history
from gdata.service import RequestError
from django.db.models import Sum
from django.db import transaction
from django.utils.translation import ugettext
from django.utils.encoding import force_unicode
from statistic.models import EmailShareStatistic
import urllib, urllib2
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from videos.rpc import VideosApiClass
from utils.rpc import RpcRouter
from utils.decorators import never_in_prod
from utils.translation import get_user_languages_from_request
from django.utils.http import urlquote_plus
from videos.tasks import video_changed_tasks
from videos.search_indexes import VideoIndex
import datetime
from icanhaz.models import VideoVisibilityPolicy
from videos.decorators import get_video_revision, get_video_from_code


rpc_router = RpcRouter('videos:rpc_router', {
    'VideosApi': VideosApiClass()
})

def index(request):
    context = widget.add_onsite_js_files({})
    context['all_videos'] = Video.objects.count()
    context['popular_videos'] = VideoIndex.get_popular_videos("-today_views")[:VideoIndex.IN_ROW]
    context['featured_videos'] = VideoIndex.get_featured_videos()[:VideoIndex.IN_ROW]
    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))

def watch_page(request):

    context = {
        'featured_videos': VideoIndex.get_featured_videos()[:VideoIndex.IN_ROW],
        'popular_videos': VideoIndex.get_popular_videos()[:VideoIndex.IN_ROW],
        'latest_videos': VideoIndex.get_latest_videos()[:VideoIndex.IN_ROW*3],
        'popular_display_views': 'week'
    }
    return render_to_response('videos/watch.html', context,
                              context_instance=RequestContext(request))

def featured_videos(request):
    return render_to_response('videos/featured_videos.html', {},
                              context_instance=RequestContext(request))

def latest_videos(request):
    return render_to_response('videos/latest_videos.html', {},
                              context_instance=RequestContext(request))

def popular_videos(request):
    return render_to_response('videos/popular_videos.html', {},
                              context_instance=RequestContext(request))

def volunteer_page(request):
    # Get the user comfort languages list
    user_langs = get_user_languages_from_request(request)

    relevant = VideoIndex.public().filter(video_language_exact__in=user_langs) \
        .filter_or(languages_exact__in=user_langs) \
        .order_by('-requests_count')

    featured_videos =  relevant.filter(
        featured__gt=datetime.datetime(datetime.MINYEAR, 1, 1)) \
        .order_by('-featured')[:5]

    popular_videos = relevant.order_by('-week_views')[:5]

    latest_videos = relevant.order_by('-edited')[:15]

    requested_videos = relevant.filter(requests_exact__in=user_langs)[:5]

    context = {
        'featured_videos': featured_videos,
        'popular_videos': popular_videos,
        'latest_videos': latest_videos,
        'requested_videos': requested_videos,
        'user_langs':user_langs,
    }

    return render_to_response('videos/volunteer.html', context,
                              context_instance=RequestContext(request))

def volunteer_category(request, category):
    '''
    Display results only for a particular category of video results from
    popular, featured and latest videos.
    '''
    return render_to_response('videos/volunteer_%s.html' %(category),
                              context_instance=RequestContext(request))

def bug(request):
    from widget.rpc import add_general_settings
    context = widget.add_config_based_js_files({}, settings.JS_API, 'unisubs-api.js')
    context['all_videos'] = Video.objects.count()
    try:
        context['video_url_obj'] = VideoUrl.objects.filter(type=VIDEO_TYPE_YOUTUBE)[:1].get()
    except VideoUrl.DoesNotExist:
        raise Http404
    general_settings = {}
    add_general_settings(request, general_settings)
    context['general_settings'] = json.dumps(general_settings)
    return render_to_response('bug.html', context,
                              context_instance=RequestContext(request))

def create(request):
    video_form = VideoForm(request.user, request.POST or None)
    context = {
        'video_form': video_form,
        'youtube_form': AddFromFeedForm(request.user)
    }
    if video_form.is_valid():
        try:
            video = video_form.save()
        except (VidscraperError, RequestError):
            context['vidscraper_error'] = True
            return render_to_response('videos/create.html', context,
                          context_instance=RequestContext(request))
        messages.info(request, message=_(u'''Here is the subtitle workspace for your video. You can
share the video with friends, or get an embed code for your site.  To add or
improve subtitles, click the button below the video.'''))

        if video_form.created:
            messages.info(request, message=_(u'''Existing subtitles will be imported in a few minutes.'''))
        return redirect(video.get_absolute_url())
    return render_to_response('videos/create.html', context,
                              context_instance=RequestContext(request))

create.csrf_exempt = True

def create_from_feed(request):
    form = AddFromFeedForm(request.user, request.POST or None)
    if form.is_valid():
        videos = form.save()
        messages.success(request, form.success_message() % {'count': len(videos)})
        return redirect('videos:create')
    context = {
        'video_form': VideoForm(),
        'youtube_form': form,
        'from_feed': True
    }
    return render_to_response('videos/create.html', context,
                              context_instance=RequestContext(request))

create_from_feed.csrf_exempt = True


@get_video_from_code
def video(request, video, video_url=None, title=None):
    """
    If user is about to perform a task on this video, then t=[task.pk]
    will be passed to as a url parameter.
    """
    if video_url:
        video_url = get_object_or_404(VideoUrl, pk=video_url)

    if not video_url and ((video.title_for_url() and not video.title_for_url() == title) or (not video.title and title)):
        return redirect(video, permanent=True)

    video.update_view_counter()

    # TODO: make this more pythonic, prob using kwargs
    context = widget.add_onsite_js_files({})
    context['video'] = video
    original = video.subtitle_language()
    context['autosub'] = 'true' if request.GET.get('autosub', False) else 'false'
    # we want a list of translations that had at least with version with subtitles
    # this will not filter subtitleversion's whos subtitles are empty
    translations = video.subtitlelanguage_set.exclude(subtitle_count=0)
    if original:
        # a video might have more than 1 is_original sl, in which case
        # we guess the right one above, but still manage to include the others
        # bellow
        translations = translations.exclude(pk=original.pk)
    translations = list(translations)
    translations.sort(key=lambda f: f.get_language_display())
    context['translations'] = translations

    context['shows_widget_sharing'] = VideoVisibilityPolicy.objects.can_show_widget(video, request.META.get('HTTP_REFERER', ''))

    context['widget_params'] = _widget_params(
        request, video, language=None,
        video_url=video_url and video_url.effective_url,
        size=(620,370)
    )

    _add_share_panel_context_for_video(context, video)
    context['lang_count'] = video.subtitlelanguage_set.filter(has_version=True).count()
    context['original'] = video.subtitle_language()
    context['task'] =  _get_related_task(request)

    return render_to_response('videos/video-view.html', context,
                              context_instance=RequestContext(request))

def _get_related_task(request):
    """
    Checks if request has t=[task-id], and if so checks if the current
    user can perform it, in case all goes well, return the task to be
    performed.
    """
    task_pk = request.GET.get('t', None)
    if task_pk:
        from teams.models import Task
        from teams.permissions import can_perform_task
        try:
            task = Task.objects.get(pk=task_pk)
            if can_perform_task(request.user, task):
                return task
        except Task.DoesNotExist:
            return

def video_list(request):
    qs = Video.objects.filter(is_subtitled=True)
    ordering = request.GET.get('o')
    order_type = request.GET.get('ot')
    extra_context = {}
    order_fields = ['languages_count', 'widget_views_count', 'subtitles_fetched_count', 'was_subtitled']
    if ordering in order_fields and order_type in ['asc', 'desc']:
        qs = qs.order_by(('-' if order_type == 'desc' else '')+ordering)
        extra_context['ordering'] = ordering
        extra_context['order_type'] = order_type
    else:
        qs = qs.order_by('-widget_views_count')
    return object_list(request, queryset=qs,
                       paginate_by=50,
                       template_name='videos/video_list.html',
                       template_object_name='video',
                       extra_context=extra_context)

def actions_list(request, video_id):
    video = get_object_or_404(Video, video_id=video_id)
    qs = Action.objects.for_video(video, request.user)

    extra_context = {
        'video': video
    }

    return object_list(request, queryset=qs, allow_empty=True,
                       paginate_by=settings.ACTIVITIES_ONPAGE,
                       template_name='videos/actions_list.html',
                       template_object_name='action',
                       extra_context=extra_context)

@login_required
@transaction.commit_manually
def upload_subtitles(request):
    output = dict(success=False)
    form = SubtitlesUploadForm(request.user, request.POST, request.FILES)

    if form.is_valid():
        try:
            language = form.save()
            output['success'] = True
            if form._sl_created:
                output['msg'] = ugettext(u'Thank you for uploading. It will take a minute or so for your subtitles to appear.')
            else:
                output['msg'] = ugettext(u'Your changes have been saved.')
            output['next'] = language.get_absolute_url()
            transaction.commit()
        except AlreadyEditingException, e:
            output['errors'] = {"_all__":[force_unicode(e.msg)]}
            transaction.rollback()
        except Exception, e:
            #trying find out one error on dev-server. hope this should help
            transaction.rollback()
            raise e
    else:
        output['errors'] = form.get_errors()
        transaction.rollback()
    return HttpResponse(u'<textarea>%s</textarea>'  % json.dumps(output))

@login_required
def paste_transcription(request):
    output = dict(success=False)
    form = PasteTranscriptionForm(request.user, request.POST)
    if form.is_valid():
        language = form.save()
        output['success'] = True
        output['next'] = language.get_absolute_url()
    else:
        output['errors'] = form.get_errors()
    return HttpResponse(json.dumps(output), "text/javascript")

@login_required
def upload_transcription_file(request):
    output = {}
    form = TranscriptionFileForm(request.POST, request.FILES)
    if form.is_valid():
        output['text'] = getattr(form, 'file_text', '')
    else:
        output['errors'] = form.get_errors()
    return HttpResponse(u'<textarea>%s</textarea>'  % json.dumps(output))

def feedback(request, hide_captcha=False):
    output = dict(success=False)
    form = FeedbackForm(request.POST, initial={'captcha': request.META['REMOTE_ADDR']},
                        hide_captcha=hide_captcha)
    if form.is_valid():
        form.send(request)
        output['success'] = True
    else:
        output['errors'] = form.get_errors()
    return HttpResponse(json.dumps(output), "text/javascript")

def site_feedback(request):
    text = request.GET.get('text', '')
    email = ''
    if request.user.is_authenticated():
        email = request.user.email
    initial = dict(message=text, email=email)
    form = FeedbackForm(initial=initial)
    return render_to_response(
        'videos/site_feedback.html', {'form':form},
        context_instance=RequestContext(request))

def email_friend(request):
    text = request.GET.get('text', '')
    link = request.GET.get('link', '')
    if link:
        text = link if not text else '%s\n%s' % (text, link)
    from_email = ''
    if request.user.is_authenticated():
        from_email = request.user.email
    initial = dict(message=text, from_email=from_email)
    if request.method == 'POST':
        form = EmailFriendForm(request.POST, auto_id="email_friend_id_%s", label_suffix="")
        if form.is_valid():
            email_st = EmailShareStatistic()
            if request.user.is_authenticated():
                email_st.user = request.user
            email_st.save()

            form.send()
            messages.info(request, 'Email Sent!')

            return redirect(request.get_full_path())
    else:
        form = EmailFriendForm(auto_id="email_friend_id_%s", initial=initial, label_suffix="")
    context = {
        'form': form
    }
    return render_to_response('videos/email_friend.html', context,
                              context_instance=RequestContext(request))

def demo(request):
    context = widget.add_onsite_js_files({})
    return render_to_response('demo.html', context,
                              context_instance=RequestContext(request))

@get_video_from_code
def legacy_history(request ,video, lang=None):
    """
    In the old days we allowed only one translation per video.
    Therefore video urls looked like /vfjdh2/en/
    Now that this constraint is removed we need to redirect old urls
    to the new view, that needs
    """
    try:
        language = video.subtitle_language(lang)
        if language is None:
            raise SubtitleLanguage.DoesNotExist("No such language")
    except SubtitleLanguage.DoesNotExist:
        raise Http404()

    return HttpResponseRedirect(reverse("videos:translation_history", kwargs={
            'video_id': video.video_id,
            'lang_id': language.pk,
            'lang': language.language,
            }))

@get_video_from_code
def history(request, video, lang=None, lang_id=None):
    if not lang:
        return HttpResponseRedirect(video.get_absolute_url(video_id=video._video_id_used))
    elif lang == 'unknown':
        # A hacky workaround for now.
        # This should go away when we stop allowing for blank SubtitleLanguages.
        lang = ''

    video.update_view_counter()

    context = widget.add_onsite_js_files({})

    if lang_id:
        try:
            language = video.subtitlelanguage_set.get(pk=lang_id)
        except SubtitleLanguage.DoesNotExist:
            raise Http404
    else:
        language = video.subtitle_language(lang)

    if not language:
        if lang in dict(settings.ALL_LANGUAGES):
            config = {}
            config["videoID"] = video.video_id
            config["languageCode"] = lang
            url = reverse('onsite_widget')+'?config='+urlquote_plus(json.dumps(config))
            return redirect(url)
        elif video.subtitlelanguage_set.count() > 0:
            language = video.subtitlelanguage_set.all()[0]
        else:
            raise Http404

    qs = language.subtitleversion_set.not_restricted_by_moderation().select_related('user')
    ordering, order_type = request.GET.get('o'), request.GET.get('ot')
    order_fields = {
        'date': 'datetime_started',
        'user': 'user__username',
        'note': 'note',
        'time': 'time_change',
        'text': 'text_change'
    }
    if ordering in order_fields and order_type in ['asc', 'desc']:
        qs = qs.order_by(('-' if order_type == 'desc' else '')+order_fields[ordering])
        context['ordering'], context['order_type'] = ordering, order_type

    context['video'] = video
    original = video.subtitle_language()
    translations = list(video.subtitlelanguage_set.filter(is_original=False) \
        .filter(had_version=True).select_related('video'))

    context["user_can_moderate"] = False

    translations.sort(key=lambda f: f.get_language_display())
    context['translations'] = translations
    context['last_version'] = language.last_version
    context['widget_params'] = _widget_params(request, video, version_no=None, language=language, size=(289,173))
    context['language'] = language
    context['edit_url'] = language.get_widget_url()
    context['shows_widget_sharing'] = VideoVisibilityPolicy.objects.can_show_widget(video, request.META.get('HTTP_REFERER', ''))

    context['task'] =  _get_related_task(request)
    _add_share_panel_context_for_history(context, video, language)
    return object_list(request, queryset=qs, allow_empty=True,
                       paginate_by=settings.REVISIONS_ONPAGE,
                       page=request.GET.get('page', 1),
                       template_name='videos/subtitle-view.html',
                       template_object_name='revision',
                       extra_context=context)

def _widget_params(request, video, version_no=None, language=None, video_url=None, size=None):
    primary_url = video_url or video.get_video_url()
    alternate_urls = [vu.effective_url for vu in video.videourl_set.all()
                      if vu.effective_url != primary_url]
    params = {'video_url': primary_url,
              'alternate_video_urls': alternate_urls,
              'base_state': {}}

    if version_no:
        params['base_state']['revision'] = version_no

    if language:
        params['base_state']['language_code'] = language.language
        params['base_state']['language_pk'] = language.pk
    if size:
        params['video_config'] = {"width":size[0], "height":size[1]}

    return base_widget_params(request, params)

@get_video_revision
def revision(request,  version):

    context = widget.add_onsite_js_files({})
    context['video'] = version.video
    context['version'] = version
    context['next_version'] = version.next_version()
    context['prev_version'] = version.prev_version()
    language = version.language
    context['language'] = language

    context["user_can_moderate"] = False
    context['widget_params'] = _widget_params(request, \
            language.video, version.version_no, language, size=(289,173))
    context['latest_version'] = language.latest_version()
    version.ordered_subtitles()
    context['rollback_allowed'] = not version.video.is_moderated
    return render_to_response('videos/revision.html', context,
                              context_instance=RequestContext(request))

@login_required
@get_video_revision
def rollback(request, version):
    if version.video.is_moderated:
        return HttpResponseForbidden("Moderated videos cannot be rollbacked, they need to be unpublished")
    is_writelocked = version.language.is_writelocked
    if is_writelocked:
        messages.error(request, u'Can not rollback now, because someone is editing subtitles.')
    elif not version.next_version():
        messages.error(request, message=u'Can not rollback to the last version')
    else:
        messages.success(request, message=u'Rollback successful')
        version = version.rollback(request.user)
        video_changed_tasks.delay(version.video.id, version.id)
        return redirect(version.language.get_absolute_url()+'#revisions')
    return redirect(version)

@get_video_revision
def diffing(request, first_version, second_pk):
    language = first_version.language
    second_version = get_object_or_404(SubtitleVersion, pk=second_pk, language=language)
    if first_version.video != second_version.video:
        # this is either a bad bug, or someone evil
        raise "Revisions for diff videos"
    video = first_version.language.video
    if second_version.datetime_started > first_version.datetime_started:
        first_version, second_version = second_version, first_version

    second_captions = dict([(item.subtitle_id, item) for item in second_version.ordered_subtitles()])
    first_captions = dict([(item.subtitle_id, item) for item in first_version.ordered_subtitles()])

    subtitles = {}

    for id, item in first_captions.items():
        if not id in subtitles:
            subtitles[id] = item.start_time

    for id, item in second_captions.items():
        if not id in subtitles:
            subtitles[id] = item.start_time

    subtitles = [item for item in subtitles.items()]
    subtitles.sort(key=lambda item: item[1])

    captions = []
    for subtitle_id, t in subtitles:
        try:
            scaption = second_captions[subtitle_id]
        except KeyError:
            scaption = None
        try:
            fcaption = first_captions[subtitle_id]
        except KeyError:
            fcaption = None

        if fcaption is None or scaption is None:
            changed = dict(text=True, time=True)
        else:
            changed = {
                'text': (not fcaption.text == scaption.text),
                'time': (not fcaption.start_time == scaption.start_time),
                'end_time': (not fcaption.end_time == scaption.end_time)
            }
        data = [fcaption, scaption, changed]
        captions.append(data)

    context = widget.add_onsite_js_files({})
    context['video'] = video
    context['captions'] = captions
    context['language'] = language
    context['first_version'] = first_version
    context['second_version'] = second_version
    context['latest_version'] = language.latest_version()
    context['rollback_allowed'] = not video.is_moderated
    context['widget0_params'] = \
        _widget_params(request, video,
                       first_version.version_no)
    context['widget1_params'] = \
        _widget_params(request, video,
                       second_version.version_no)
    return render_to_response('videos/diffing.html', context,
                              context_instance=RequestContext(request))

def test_form_page(request):
    if request.method == 'POST':
        form = UserTestResultForm(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request, 'Thanks for your feedback.  It\'s a huge help to us as we improve the site.')
            return redirect('videos:test_form_page')
    else:
        form = UserTestResultForm()
    context = {
        'form': form
    }
    return render_to_response('videos/test_form_page.html', context,
                              context_instance=RequestContext(request))

@login_required
def stop_notification(request, video_id):
    user_id = request.GET.get('u')
    hash = request.GET.get('h')

    if not user_id or not hash:
        raise Http404

    video = get_object_or_404(Video, video_id=video_id)
    user = get_object_or_404(User, id=user_id)
    context = dict(video=video, u=user)

    if hash and user.hash_for_video(video_id) == hash:
        video.followers.remove(user)
        for l in video.subtitlelanguage_set.all():
            l.followers.remove(user)
        if request.user.is_authenticated() and not request.user == user:
            logout(request)
    else:
        context['error'] = u'Incorrect secret hash'
    return render_to_response('videos/stop_notification.html', context,
                              context_instance=RequestContext(request))

def counter(request):
    count = Video.objects.aggregate(c=Sum('subtitles_fetched_count'))['c']
    return HttpResponse('draw_unisub_counter({videos_count: %s})' % count)

@login_required
def video_url_make_primary(request):
    output = {}

    id = request.GET.get('id')
    if id:
        try:
            obj = VideoUrl.objects.get(id=id)
            if not obj.video.allow_video_urls_edit and not request.user.has_perm('videos.change_videourl'):
                output['error'] = ugettext('You have not permission change this URL')
            else:
                VideoUrl.objects.filter(video=obj.video).update(primary=False)
                obj.primary = True
                obj.save(updates_timestamp=False)
        except VideoUrl.DoesNotExist:
            output['error'] = ugettext('Object does not exist')
    return HttpResponse(json.dumps(output))

@login_required
def video_url_remove(request):
    output = {}
    id = request.GET.get('id')

    if id:
        try:
            obj = VideoUrl.objects.get(id=id)

            if not obj.video.allow_video_urls_edit and not request.user.has_perm('videos.delete_videourl'):
                output['error'] = ugettext('You have not permission delete this URL')
            else:
                if obj.original:
                    output['error'] = ugettext('You cann\'t remove original URL')
                else:
                    obj.delete()
        except VideoUrl.DoesNotExist:
            output['error'] = ugettext('Object does not exist')
    return HttpResponse(json.dumps(output))

@login_required
def video_url_create(request):
    output = {}

    form = CreateVideoUrlForm(request.user, request.POST)
    if form.is_valid():
        obj = form.save()
        video = form.cleaned_data['video']
        users = video.notification_list(request.user)

        for user in users:
            subject = u'New video URL added by %(username)s to "%(video_title)s" on universalsubtitles.org'
            subject = subject % {'url': obj.url, 'username': obj.added_by, 'video_title': video}
            context = {
                'video': video,
                'video_url': obj,
                'user': user,
                'domain': Site.objects.get_current().domain,
                'hash': user.hash_for_video(video.video_id)
            }
            send_templated_email(user, subject,
                                 'videos/email_video_url_add.html',
                                 context, fail_silently=not settings.DEBUG)
    else:
        output['errors'] = form.get_errors()

    return HttpResponse(json.dumps(output))

def subscribe_to_updates(request):
    email_address = request.POST.get('email_address', '')
    data = urllib.urlencode({'email': email_address})
    req = urllib2.Request(
        'http://pcf8.pculture.org/interspire/form.php?form=3', data)
    urllib2.urlopen(req)
    return HttpResponse('ok', 'text/plain')

def test_celery(request):
    from videos.tasks import add
    add.delay(1, 2)
    return HttpResponse('Hello, from Amazon SQS backend for Celery!')

@staff_member_required
def test_celery_exception(request):
    from videos.tasks import raise_exception
    raise_exception.delay('Exception in Celery', should_be_logged='Hello, man!')
    return HttpResponse('Hello, from Amazon SQS backend for Celery! Look for exception.')

@never_in_prod
@staff_member_required
def video_staff_delete(request, video_id):
    video = get_object_or_404(Video, video_id=video_id)
    video.delete()
    return HttpResponse("ok")

def video_debug(request, video_id):
    from apps.testhelpers.views import debug_video
    from apps.widget import video_cache as vc
    from django.core.cache import cache
    video = get_object_or_404(Video, video_id=video_id)
    lang_info = debug_video(video)
    vid = video.video_id
    get_subtitles_dict = {}
    for l in video.subtitlelanguage_set.all():
        cache_key = vc._subtitles_dict_key(vid, l.pk, None)
        get_subtitles_dict[l.language] = cache.get(cache_key)
    cache = {
        "get_video_urls": cache.get(vc._video_urls_key(vid)),
        "get_subtitles_dict": get_subtitles_dict,
        "get_video_languages": cache.get(vc._video_languages_key(vid)),

        "get_video_languages_verbose": cache.get(vc._video_languages_verbose_key(vid)),
        "writelocked_langs": cache.get(vc._video_writelocked_langs_key(vid)),
    }
    return render_to_response("videos/video_debug.html", {
            'video':video,
            'lang_info': lang_info,
            "cache": cache
    }, context_instance=RequestContext(request))

def reset_metadata(request, video_id):
    video = get_object_or_404(Video, video_id=video_id)
    video_changed_tasks.delay(video.id)
    return HttpResponse('ok')

