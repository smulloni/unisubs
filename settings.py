# Universal Subtitles, universalsubtitles.org
# 
# Copyright (C) 2010 Participatory Culture Foundation
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

# Django settings for unisubs project.
import os, sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def rel(*x):
    return os.path.join(PROJECT_ROOT, *x)

gettext_noop = lambda s: s

from django.conf import global_settings
#: see doc/i18n

METADATA_LANGUAGES = (
    ('meta-tw', 'Metadata: Twitter'),
    ('meta-geo', 'Metadata: Geo'),
    ('meta-wiki', 'Metadata: Wikipedia'),
)

ALL_LANGUAGES = list(global_settings.LANGUAGES)
ALL_LANGUAGES.extend(METADATA_LANGUAGES)
ALL_LANGUAGES = dict(ALL_LANGUAGES)


ALL_LANGUAGES[ 'aa']= gettext_noop(u'Afar')
ALL_LANGUAGES['ab']= gettext_noop( u'Abkhazian')
ALL_LANGUAGES['ae']= gettext_noop( u'Avestan')
ALL_LANGUAGES['af'] = gettext_noop(u'Afrikaans')
ALL_LANGUAGES['aka'] = gettext_noop(u'Akan')
ALL_LANGUAGES['amh'] = gettext_noop(u'Amharic')
ALL_LANGUAGES['an']= gettext_noop( u'Aragonese')
ALL_LANGUAGES['as'] = gettext_noop(u'Assamese')
ALL_LANGUAGES['ase'] = gettext_noop(u'American Sign Language')
ALL_LANGUAGES['ast'] = gettext_noop(u'Asturian')
ALL_LANGUAGES['av']= gettext_noop( u'Avaric')
ALL_LANGUAGES['ay'] = gettext_noop(u'Aymara')
ALL_LANGUAGES['ba']= gettext_noop( u'Bashkir')
ALL_LANGUAGES['bam'] = gettext_noop(u'Bambara')
ALL_LANGUAGES['be'] = gettext_noop(u'Belarusian')
ALL_LANGUAGES['ber'] = gettext_noop(u'Berber')
ALL_LANGUAGES['bh']= gettext_noop( u'Bihari')
ALL_LANGUAGES['bi'] = gettext_noop(u'Bislama')
ALL_LANGUAGES['bnt'] = gettext_noop(u'Ibibio')
ALL_LANGUAGES['bo'] = gettext_noop(u'Tibetan')
ALL_LANGUAGES['br'] = gettext_noop(u'Breton')
ALL_LANGUAGES['ce']= gettext_noop( u'Chechen')
ALL_LANGUAGES['ceb'] = gettext_noop(u'Cebuan')
ALL_LANGUAGES['ch']= gettext_noop( u'Chamorro')
ALL_LANGUAGES['cho']= gettext_noop( 'Choctaw')
ALL_LANGUAGES['co']= gettext_noop( u'Corsican')
ALL_LANGUAGES['cr'] = gettext_noop(u'Cree')
ALL_LANGUAGES['cu']= gettext_noop( u'Church Slavic')
ALL_LANGUAGES['cv']= gettext_noop( u'Chuvash')
ALL_LANGUAGES['dv']= gettext_noop( u'Divehi')
ALL_LANGUAGES['dz']= gettext_noop( u'Dzongkha')
ALL_LANGUAGES['ee'] = gettext_noop(u'Ewe')
ALL_LANGUAGES['efi']= gettext_noop( 'Efik')
ALL_LANGUAGES['en-gb'] = gettext_noop(u'English, British')
ALL_LANGUAGES['eo'] = gettext_noop(u'Esperanto')
ALL_LANGUAGES['eo'] = gettext_noop(u'Esperanto')
ALL_LANGUAGES['es-ar'] = gettext_noop(u'Spanish, Argentinian')
ALL_LANGUAGES['es-mx'] = gettext_noop(u'Spanish, Mexican')
ALL_LANGUAGES['es-ni'] = gettext_noop(u'Spanish, Nicaraguan')
ALL_LANGUAGES['ff']= gettext_noop( u'Fulah')
ALL_LANGUAGES['fil'] = gettext_noop(u'Filipino')
ALL_LANGUAGES['fj']= gettext_noop( u'Fijian')
ALL_LANGUAGES['fo']= gettext_noop( u'Faroese')
ALL_LANGUAGES['fr-ca'] = gettext_noop(u'French, Canadian')
ALL_LANGUAGES['ful'] = gettext_noop(u'Fula')
ALL_LANGUAGES['gd']= gettext_noop( u'Scottish Gaelic')
ALL_LANGUAGES['gn']= gettext_noop( u'Guaran')
ALL_LANGUAGES['gu'] = gettext_noop(u'Gujarati')
ALL_LANGUAGES['gv']= gettext_noop( u'Manx')
ALL_LANGUAGES['hai'] = gettext_noop(u'Haida')
ALL_LANGUAGES['hau'] = gettext_noop(u'Hausa')
ALL_LANGUAGES['ho']= gettext_noop( u'Hiri Motu')
ALL_LANGUAGES['ht'] = gettext_noop(u'Creole, Haitian')
ALL_LANGUAGES['hup']= gettext_noop( 'Hupa')
ALL_LANGUAGES['hy'] = gettext_noop(u'Armenian')
ALL_LANGUAGES['hz']= gettext_noop( u'Herero')
ALL_LANGUAGES['ia']= gettext_noop( u'Interlingua')
ALL_LANGUAGES['ibo'] = gettext_noop(u'Igbo')
ALL_LANGUAGES['ie']= gettext_noop( u'Interlingue')
ALL_LANGUAGES['ii']= gettext_noop( u'Sichuan Yi')
ALL_LANGUAGES['ik']= gettext_noop( u'Inupia')
ALL_LANGUAGES['ilo'] = gettext_noop(u'Ilocano')
ALL_LANGUAGES['inh']= gettext_noop( 'Ingush')
ALL_LANGUAGES['io']= gettext_noop( u'Ido')
ALL_LANGUAGES['iro'] = gettext_noop(u'Iroquoian languages')
ALL_LANGUAGES['iu'] = gettext_noop(u'Inuktitut')
ALL_LANGUAGES['jv']= gettext_noop( u'Javanese')
ALL_LANGUAGES['ka'] = gettext_noop(u'Georgian')
ALL_LANGUAGES['kar'] = gettext_noop(u'Karen')
ALL_LANGUAGES['kau'] = gettext_noop(u'Kanuri')
ALL_LANGUAGES['kik'] = gettext_noop(u'Gikuyu')
ALL_LANGUAGES['kin'] = gettext_noop(u'Kinyarwanda')
ALL_LANGUAGES['kj']= gettext_noop( u'Kuanyama, Kwanyama')
ALL_LANGUAGES['kk'] = gettext_noop(u'Kazakh')
ALL_LANGUAGES['kl']= gettext_noop( u'Kalaallisut')
ALL_LANGUAGES['kon'] = gettext_noop(u'Kongo')
ALL_LANGUAGES['ks']= gettext_noop( u'Kashmiri')
ALL_LANGUAGES['ku']= gettext_noop( u'Kurdish')
ALL_LANGUAGES['kv']= gettext_noop( u'Komi')
ALL_LANGUAGES['kw'] = gettext_noop(u'Cornish')
ALL_LANGUAGES['ky'] = gettext_noop(u'Kyrgyz')
ALL_LANGUAGES['la']= gettext_noop( u'Latin')
ALL_LANGUAGES['lb']= gettext_noop( u'Luxembourgish')
ALL_LANGUAGES['lg']= gettext_noop( u'Ganda')
ALL_LANGUAGES['li']= gettext_noop( u'Limburgish')
ALL_LANGUAGES['lin'] = gettext_noop(u'Lingala')
ALL_LANGUAGES['lkt'] = gettext_noop(u'Lakota')
ALL_LANGUAGES['lo'] = gettext_noop(u'Lao')
ALL_LANGUAGES['lu']= gettext_noop( u'Luba-Katagana')
ALL_LANGUAGES['lua'] = gettext_noop(u'Luba-Kasai')
ALL_LANGUAGES['luo'] = gettext_noop(u'Luo')
ALL_LANGUAGES['luy'] = gettext_noop(u'Luhya')
ALL_LANGUAGES['mad']= gettext_noop( u'Madurese')
ALL_LANGUAGES['mh']= gettext_noop( u'Marshallese')
ALL_LANGUAGES['mi']= gettext_noop( u'Maori')
ALL_LANGUAGES['ml'] = gettext_noop(u'Malayalam')
ALL_LANGUAGES['mlg'] = gettext_noop(u'Malagasy')
ALL_LANGUAGES['mnk'] = gettext_noop(u'Mandinka')
ALL_LANGUAGES['mo']= gettext_noop( u'Moldavian, Moldovan')
ALL_LANGUAGES['moh'] = gettext_noop(u'Mohawk')
ALL_LANGUAGES['mos'] = gettext_noop(u'Mossi')
ALL_LANGUAGES['mr'] = gettext_noop(u'Marathi')
ALL_LANGUAGES['ms'] = gettext_noop(u'Malay')
ALL_LANGUAGES['mt'] = gettext_noop(u'Maltese')
ALL_LANGUAGES['my'] = gettext_noop(u'Burmese')
ALL_LANGUAGES['na']= gettext_noop( u'Naurunan')
ALL_LANGUAGES['nan']= gettext_noop( u'Hokkien')
ALL_LANGUAGES['nb'] = gettext_noop(u'Norwegian, Bokmal')
ALL_LANGUAGES['nd']= gettext_noop( u'North Ndebele')
ALL_LANGUAGES['ne'] = gettext_noop(u'Nepali')
ALL_LANGUAGES['ng']= gettext_noop( u'Ndonga')
ALL_LANGUAGES['nn'] = gettext_noop(u'Norwegian, Nynorsk')
ALL_LANGUAGES['no']= gettext_noop( u'Norwegian')
ALL_LANGUAGES['nr']= gettext_noop( u'Southern Ndebele')
ALL_LANGUAGES['nso'] = gettext_noop(u'Northern Sotho')
ALL_LANGUAGES['nv']= gettext_noop( u'Navajo')
ALL_LANGUAGES['nya'] = gettext_noop(u'Chewa')
ALL_LANGUAGES['oc'] = gettext_noop(u'Occitan')
ALL_LANGUAGES['oji'] = gettext_noop(u'Anishinaabe')
ALL_LANGUAGES['or'] = gettext_noop(u'Oriya')
ALL_LANGUAGES['orm'] = gettext_noop(u'Oromo')
ALL_LANGUAGES['os']= gettext_noop( u'Ossetian, Ossetic')
ALL_LANGUAGES['pi']= gettext_noop( u'Pali')
ALL_LANGUAGES['ps'] = gettext_noop(u'Pashto')
ALL_LANGUAGES['pt-br'] = gettext_noop(u'Portuguese, Brazilian')
ALL_LANGUAGES['que'] = gettext_noop(u'Quechua')
ALL_LANGUAGES['rm']= gettext_noop( u'Romansh')
ALL_LANGUAGES['run']= gettext_noop( u'Rundi')
ALL_LANGUAGES['rup'] = gettext_noop(u'Macedo (Aromanian) Romanian')
ALL_LANGUAGES['ry']= gettext_noop( u'Rusyn')
ALL_LANGUAGES['sa']= gettext_noop( u'Sanskrit')
ALL_LANGUAGES['sc']= gettext_noop( u'Sardinian')
ALL_LANGUAGES['sd']= gettext_noop( u'Sindhi')
ALL_LANGUAGES['se']= gettext_noop( u'Northern Sami')
ALL_LANGUAGES['sg']= gettext_noop( u'Sango')
ALL_LANGUAGES['sh'] = gettext_noop(u'Serbo-Croatian')
ALL_LANGUAGES['si'] = gettext_noop(u'Sinhala')
ALL_LANGUAGES['sm']= gettext_noop( u'Samoan')
ALL_LANGUAGES['sna'] = gettext_noop(u'Shona')
ALL_LANGUAGES['som'] = gettext_noop(u'Somali')
ALL_LANGUAGES['sot'] = gettext_noop(u'Sotho')
ALL_LANGUAGES['sr-latn'] = gettext_noop(u'Serbian, Latin')
ALL_LANGUAGES['ss']= gettext_noop( u'Swati')
ALL_LANGUAGES['su']= gettext_noop( u'Sundanese')
ALL_LANGUAGES['swa'] = gettext_noop(u'Swahili')
ALL_LANGUAGES['tg']= gettext_noop( u'Tajik')
ALL_LANGUAGES['tet']= gettext_noop( u'Tetum')
ALL_LANGUAGES['tir'] = gettext_noop(u'Tigrinya')
ALL_LANGUAGES['tk']= gettext_noop( u'Turkmen')
ALL_LANGUAGES['tl'] = gettext_noop(u'Tagalog')
ALL_LANGUAGES['tlh'] = gettext_noop(u'Klingon')
ALL_LANGUAGES['to']= gettext_noop( u'Tonga')
ALL_LANGUAGES['ts']= gettext_noop( u'Tsonga')
ALL_LANGUAGES['tsn'] = gettext_noop(u'Tswana')
ALL_LANGUAGES['tt']= gettext_noop( u'Tartar')
ALL_LANGUAGES['tw']= gettext_noop( u'Twi')
ALL_LANGUAGES['ty']= gettext_noop( u'Tahitian')
ALL_LANGUAGES['ug']= gettext_noop( u'Uighur')
ALL_LANGUAGES['umb'] = gettext_noop(u'Umbundu')
ALL_LANGUAGES['uz'] = gettext_noop(u'Uzbek')
ALL_LANGUAGES['ve']= gettext_noop( u'Venda')
ALL_LANGUAGES['vo']= gettext_noop( u'Volapuk')
ALL_LANGUAGES['wa']= gettext_noop( u'Walloon')
ALL_LANGUAGES['wol'] = gettext_noop(u'Wolof')
ALL_LANGUAGES['xho'] = gettext_noop(u'Xhosa')
ALL_LANGUAGES['yi'] = gettext_noop(u'Yiddish')
ALL_LANGUAGES['yor'] = gettext_noop(u'Yoruba')
ALL_LANGUAGES['za']= gettext_noop( u'Zhuang, Chuang:')
ALL_LANGUAGES['zh'] = gettext_noop(u'Chinese, Yue')
ALL_LANGUAGES['zh-cn'] = gettext_noop(u'Chinese, Simplified')
ALL_LANGUAGES['zh-tw'] = gettext_noop(u'Chinese, Traditional')
ALL_LANGUAGES['zul'] = gettext_noop(u'Zulu')

if ALL_LANGUAGES.get('no', None):
    del ALL_LANGUAGES['no']
    
full_langs = dict(ALL_LANGUAGES.items())
ALL_LANGUAGES = tuple(i for i in ALL_LANGUAGES.items())
# this has to be set after all languages have been appended
global_settings.LANGUAGES = tuple(i for i in full_langs.items())
# languages that more people speak, and therefore
# are it's translators are not as rare
LINGUA_FRANCAS = ["en", "en-gb"]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PISTON_EMAIL_ERRORS = True
PISTON_DISPLAY_ERRORS = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

ALARM_EMAIL = None
MANAGERS = ADMINS

P3P_COMPACT = 'CP="CURa ADMa DEVa OUR IND DSP CAO COR"'

DEFAULT_FROM_EMAIL = '"Universal Subtitles" <feedback@universalsubtitles.org>'
WIDGET_LOG_EMAIL = 'widget-logs@universalsubtitles.org'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('unisubs.sqlite3'), # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# 'embed{0}.js'.format(EMBED_JS_VERSION) gives the current embed script file name.
EMBED_JS_VERSION = ''
PREVIOUS_EMBED_JS_VERSIONS = []

CSS_USE_COMPILED = True

USE_BUNDLED_MEDIA = not DEBUG

COMPRESS_YUI_BINARY = "java -jar ./css-compression/yuicompressor-2.4.6.jar"
COMPRESS_OUTPUT_DIRNAME = "static-cache"


USER_LANGUAGES_COOKIE_NAME = 'unisub-languages-cookie'

# paths provided relative to media/js
JS_CORE = \
    ['js/unisubs.js', 
     'js/rpc.js',
     'js/clippy.js',
     'js/flash.js',
     'js/spinner.js',
     'js/sliderbase.js',
     'js/closingwindow.js',
     'js/loadingdom.js',
     'js/tracker.js',
     'js/style.js',
     'js/messaging/simplemessage.js',
     'js/player/video.js',
     'js/player/captionview.js',
     'js/widget/usersettings.js',
     'js/player/abstractvideoplayer.js',
     'js/player/flashvideoplayer.js',
     'js/player/html5mediaplayer.js',
     'js/player/html5videoplayer.js',
     'js/player/html5audioplayer.js',
     'js/player/youtubevideoplayer.js',
     'js/player/ytiframevideoplayer.js',
     'js/player/youtubebasemixin.js',
     'js/player/jwvideoplayer.js',
     'js/player/flvvideoplayer.js',
     'js/player/flashaudioplayer.js',
     'js/player/mediasource.js',
     'js/player/mp3source.js',
     'js/player/html5videosource.js',
     'js/player/youtubevideosource.js',
     'js/player/ytiframevideosource.js',
     'js/player/brightcovevideosource.js',
     'js/player/brightcovevideoplayer.js',
     'js/player/flvvideosource.js',
     'js/player/bliptvplaceholder.js',
     'js/player/controlledvideoplayer.js',
     'js/player/vimeovideosource.js',
     'js/player/vimeovideoplayer.js',
     'js/player/dailymotionvideosource.js',
     'js/player/dailymotionvideoplayer.js',
     'js/startdialog/model.js',
     'js/startdialog/videolanguage.js',
     'js/startdialog/videolanguages.js',
     'js/startdialog/tolanguage.js',
     'js/startdialog/tolanguages.js',
     'js/startdialog/dialog.js',
     'js/streamer/streambox.js', 
     'js/streamer/streamboxsearch.js', 
     'js/streamer/streamsub.js', 
     'js/streamer/streamervideotab.js', 
     'js/streamer/streamerdecorator.js', 
     'js/requestdialog.js',
     'js/widget/videotab.js',
     'js/widget/hangingvideotab.js',
     'js/widget/subtitle/editablecaption.js',
     "js/widget/subtitle/editablecaptionset.js",
     'js/widget/logindialog.js',
     'js/widget/howtovideopanel.js',
     'js/widget/guidelinespanel.js',
     'js/widget/dialog.js',
     'js/widget/captionmanager.js',
     'js/widget/rightpanel.js',
     'js/widget/basestate.js',
     'js/widget/subtitlestate.js',
     'js/widget/dropdowncontents.js',
     'js/widget/playcontroller.js',
     'js/widget/subtitlecontroller.js',
     'js/widget/subtitledialogopener.js',
     'js/widget/opendialogargs.js',
     'js/widget/dropdown.js',
     'js/widget/resumeeditingrecord.js',
     'js/widget/resumedialog.js',
     'js/widget/subtitle/savedsubtitles.js',
     'js/widget/play/manager.js',
     'js/widget/widgetcontroller.js',
     'js/widget/widget.js'
]

JS_DIALOG = \
    ['js/subtracker.js',
     'js/srtwriter.js',
     'js/widget/unsavedwarning.js',
     'js/widget/emptysubswarningdialog.js',
     'js/widget/droplockdialog.js',
     'js/finishfaildialog/dialog.js',
     'js/finishfaildialog/errorpanel.js',
     'js/finishfaildialog/reattemptuploadpanel.js',
     'js/finishfaildialog/copydialog.js',
     'js/widget/reviewsubtitles/dialog.js',
     'js/widget/reviewsubtitles/reviewsubtitlespanel.js',
     'js/widget/reviewsubtitles/reviewsubtitlesrightpanel.js',
     'js/widget/approvesubtitles/dialog.js',
     'js/widget/approvesubtitles/approvesubtitlespanel.js',
     'js/widget/approvesubtitles/approvesubtitlesrightpanel.js',
     'js/widget/editmetadata/dialog.js',
     'js/widget/editmetadata/panel.js',
     'js/widget/editmetadata/editmetadatarightpanel.js',
     'js/widget/subtitle/dialog.js',
     'js/widget/subtitle/msservermodel.js',
     'js/widget/subtitle/subtitlewidget.js',
     'js/widget/subtitle/addsubtitlewidget.js',
     'js/widget/subtitle/subtitlelist.js',
     'js/widget/subtitle/transcribeentry.js',
     'js/widget/subtitle/transcribepanel.js',
     'js/widget/subtitle/transcriberightpanel.js',
     'js/widget/subtitle/syncpanel.js',
     'js/widget/subtitle/reviewpanel.js',
     'js/widget/subtitle/reviewrightpanel.js',
     'js/widget/subtitle/sharepanel.js',
     'js/widget/subtitle/completeddialog.js',
     'js/widget/subtitle/editpanel.js',
     'js/widget/subtitle/onsaveddialog.js',
     'js/widget/subtitle/editrightpanel.js',
     'js/widget/subtitle/bottomfinishedpanel.js',
     'js/widget/subtitle/logger.js',
     'js/widget/timeline/timerow.js',
     'js/widget/timeline/timerowul.js',
     'js/widget/timeline/timelinesub.js',
     'js/widget/timeline/timelinesubs.js',
     'js/widget/timeline/timelineinner.js',
     'js/widget/timeline/timeline.js',
     'js/widget/timeline/subtitle.js',
     'js/widget/timeline/subtitleset.js',
     'js/widget/controls/bufferedbar.js',
     'js/widget/controls/playpause.js',
     'js/widget/controls/progressbar.js',
     'js/widget/controls/progressslider.js',
     'js/widget/controls/timespan.js',
     'js/widget/controls/videocontrols.js',
     'js/widget/controls/volumecontrol.js',
     'js/widget/controls/volumeslider.js',
     'js/widget/translate/bingtranslator.js',
     'js/widget/translate/dialog.js',
     'js/widget/translate/translationpanel.js',
     'js/widget/translate/translationlist.js',
     'js/widget/translate/translationwidget.js',
     'js/widget/translate/descriptiontranslationwidget.js',
     'js/widget/translate/translationrightpanel.js',
     'js/widget/translate/forkdialog.js',
     'js/widget/translate/titletranslationwidget.js']

JS_OFFSITE = list(JS_CORE)
JS_OFFSITE.append('js/widget/crossdomainembed.js')

JS_ONSITE = list(JS_CORE)
JS_ONSITE.extend(
    ['js/srtwriter.js',
     'js/widget/samedomainembed.js',
     "js/widget/api/servermodel.js",
     "js/widget/api/api.js"])

JS_WIDGETIZER_CORE = list(JS_CORE)
JS_WIDGETIZER_CORE.extend([
    "js/widget/widgetdecorator.js",
    "js/widgetizer/videoplayermaker.js",
    "js/widgetizer/widgetizer.js",
    "js/widgetizer/youtube.js",
    "js/widgetizer/html5.js",
    "js/widgetizer/jwplayer.js",
    "js/widgetizer/youtubeiframe.js",
    "js/widgetizer/wistia.js",
    "js/widgetizer/soundcloud.js",
    'js/player/ooyalaplayer.js', 
    'js/player/wistiavideoplayer.js', 
    'js/player/brightcoveliteplayer.js', 
    'js/player/soundcloudplayer.js',
    'js/streamer/overlaycontroller.js'])

JS_WIDGETIZER = list(JS_WIDGETIZER_CORE)
JS_WIDGETIZER.append('js/widgetizer/dowidgetize.js')

JS_EXTENSION = list(JS_WIDGETIZER_CORE)
JS_EXTENSION.append('js/widgetizer/extension.js')

JS_API = list(JS_CORE)
JS_API.extend(JS_DIALOG)
JS_API.extend([
        "js/widget/api/servermodel.js",
        "js/widget/api/api.js"])

JS_BASE_DEPENDENCIES = [
    'js/closure-library/closure/goog/base.js',
    'js/closure-dependencies.js',
    'js/swfobject.js',
    'flowplayer/flowplayer-3.2.6.min.js',
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
STATIC_ROOT = rel('media')+'/'
MEDIA_ROOT  = rel('user-data')+'/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)


MIDDLEWARE_CLASSES = (
    'middleware.ResponseTimeMiddleware',
    'utils.ajaxmiddleware.AjaxErrorMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    'middleware.P3PHeaderMiddleware',
    'middleware.UserUUIDMiddleware',
    'middleware.SaveUserIp',
)

ROOT_URLCONF = 'unisubs.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
   rel('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'context_processors.current_site',
    'context_processors.current_commit',
    'context_processors.custom',
    'context_processors.user_languages',
    'context_processors.run_locally',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'utils.context_processors.media',
)

INSTALLED_APPS = (
    # this needs to be first, yay for app model loading mess
    'auth',
    # django stock apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.webdesign',
    # third party apps
    'django_extensions',
    'djcelery',
    'haystack',
    'indexer',
    'livesettings',
    'paging',
    'rosetta',
    'sentry',
    'sentry.client',
    'sorl.thumbnail',
    'south',
    'tastypie',
    # third party apps forked on our repo
    'localeurl',
    'openid_consumer',
    'socialauth',
    # our apps
    'accountlinker',
    'comments',
    'doorman',
    'icanhaz',
    'messages',
    'profiles',
    'search',
    'statistic',
    'streamer',
    'teams',
    'testhelpers',
    'unisubs', #dirty hack to fix http://code.djangoproject.com/ticket/5494 ,
    'unisubs_compressor',
    'uslogging',
    'utils',
    'videos',
    'widget',
)

# Celery settings

# import djcelery
# djcelery.setup_loader()

# For running worker use: python manage.py celeryd -E --concurrency=10 -n worker1.localhost
# Run event cather for monitoring workers: python manage.py celerycam --frequency=5.0
# This allow know are workers online or not: python manage.py celerybeat

CELERY_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = True
CELERY_SEND_EVENTS = False
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_RESULT_BACKEND = 'redis'

BROKER_BACKEND = 'kombu_backends.amazonsqs.Transport'
BROKER_USER = AWS_ACCESS_KEY_ID = ""
BROKER_PASSWORD = AWS_SECRET_ACCESS_KEY = ""
BROKER_HOST = "localhost"
BROKER_POOL_LIMIT = 10

#################

import re
LOCALE_INDEPENDENT_PATHS = (
    re.compile('^/widget'),
    re.compile('^/api'),
    re.compile('^/api2'),
    re.compile('^/jstest'),
    re.compile('^/sitemap.*.xml'),
    re.compile('^/accountlinker/youtube-oauth-callback/'),
    #re.compile('^/crossdomain.xml'),
)

#Haystack configuration
HAYSTACK_SITECONF = 'search_site'
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
SOLR_ROOT = rel('..', 'buildout', 'parts', 'solr', 'example')

# socialauth-related
OPENID_REDIRECT_NEXT = '/socialauth/openid/done/'

OPENID_SREG = {"required": "nickname, email", "optional":"postcode, country", "policy_url": ""}
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email", "count": 1, "required": True, "alias": "email"},
             {"type_uri": "fullname", "count": 1 , "required": False, "alias": "fullname"}]

FACEBOOK_API_KEY = ''
FACEBOOK_SECRET_KEY = ''

VIMEO_API_KEY = None
VIMEO_API_SECRET = None

AUTHENTICATION_BACKENDS = (
   'auth.backends.CustomUserBackend',
   'auth.backends.OpenIdBackend',
   'auth.backends.TwitterBackend',
   'auth.backends.FacebookBackend',
   'django.contrib.auth.backends.ModelBackend',
)

SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = 'profiles.Profile'
ACCOUNT_ACTIVATION_DAYS = 9999 # we are using registration only to verify emails
SESSION_COOKIE_AGE = 2419200 # 4 weeks

RECENT_ACTIVITIES_ONPAGE = 10
ACTIVITIES_ONPAGE = 20
REVISIONS_ONPAGE = 20

FEEDBACK_EMAIL = 'socmedia@pculture.org'
FEEDBACK_EMAILS = [FEEDBACK_EMAIL]
FEEDBACK_ERROR_EMAIL = 'universalsubtitles-errors@pculture.org'
FEEDBACK_SUBJECT = 'Universal Subtitles Feedback'
FEEDBACK_RESPONSE_SUBJECT = 'Thanks for trying Universal Subtitles'
FEEDBACK_RESPONSE_EMAIL = 'universalsubtitles@pculture.org'
FEEDBACK_RESPONSE_TEMPLATE = 'feedback_response.html'

#teams
TEAMS_ON_PAGE = 12

PROJECT_VERSION = '0.5'

EDIT_END_THRESHOLD = 120

ANONYMOUS_USER_ID = 10000

#Use on production
GOOGLE_ANALYTICS_NUMBER = 'UA-163840-22'
MIXPANEL_TOKEN = '44205f56e929f08b602ccc9b4605edc3'

try:
    from commit import LAST_COMMIT_GUID
except ImportError:
    sys.stderr.write("deploy/create_commit_file must be ran before boostrapping django")
    LAST_COMMIT_GUID = "dev/dev"

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
DEFAULT_BUCKET = ''
AWS_USER_DATA_BUCKET_NAME  = ''
USE_AMAZON_S3 = AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and DEFAULT_BUCKET


AVATAR_MAX_SIZE = 500*1024
THUMBNAILS_SIZE = (
    (100, 100),
    (50, 50),
    (120, 90)
)

EMAIL_BCC_LIST = []

CACHE_BACKEND = 'locmem://'

#for unisubs.example.com
RECAPTCHA_PUBLIC = '6LdoScUSAAAAANmmrD7ALuV6Gqncu0iJk7ks7jZ0'
RECAPTCHA_SECRET = ' 6LdoScUSAAAAALvQj3aI1dRL9mHgh85Ks2xZH1qc'

ROSETTA_EXCLUDED_APPLICATIONS = (
    'livesettings',
    'openid_consumer',
    'rosetta'
)

# paths from MEDIA URL
MEDIA_BUNDLES = {

    "base": {
        "type":"css",
        "files" : (
            "css/jquery.jgrowl.css",
            "css/jquery.alerts.css",
            "css/960.css",
            "css/reset.css",
            "css/html.css", 
            "css/about_faq.css", 
            "css/breadcrumb.css", 
            "css/buttons.css",
            "css/chosen.css",
            "css/classes.css", 
            "css/forms.css",
            "css/index.css",
            "css/layout.css",
            "css/profile_pages.css", 
            "css/revision_history.css",
            "css/teams.css", 
            "css/transcripts.css", 
            "css/background.css", 
            "css/activity_stream.css", 
            "css/settings.css", 
            "css/feedback.css", 
            "css/messages.css", 
            "css/global.css", 
            "css/top_user_panel.css", 
            "css/services.css", 
            "css/solutions.css",
            "css/watch.css",
            "css/v1.css",
            "css/bootstrap.css",
          ),
        },
    "video_history":{
        "type":"css",
        "files":(
               "css/unisubs-widget.css" ,
               "css/dev.css"
         ),
        },

    "jquery-ui":{
        "type":"css",
        "files":(
               "css/jquery-ui/jquery-ui-1.8.16.custom.css",
         ),
        },

    "home":{
        "type":"css",
        "files":(
            "css/unisubs-widget.css",
         ),
        },
     "new_home":{
         "type":"css",
         "files":(
            "css/new_index.css",
             "css/unisubs-widget.css",
          ),
         },
    "widget-css":{
         "type":"css",
         "files":(
             "css/unisubs-widget.css",
          ),
        },
    "unisubs-offsite-compiled":{
        "type": "js",
        "files": JS_OFFSITE,
        },

    "unisubs-onsite-compiled":{
        "type": "js",
        "files": JS_ONSITE,
     },
    "unisubs-widgetizer":{
        "type": "js",
        "closure_deps": "js/closure-dependencies.js",
        "files": ["js/config.js"] + JS_WIDGETIZER,
        "bootloader": { 
            "template": "widget/widgetizerbootloader.js",
            "gatekeeper": "UnisubsWidgetizerLoaded",
            "render_bootloader": True
        }
    },
    "unisubs-widgetizer-sumo": {
        "type": "js",
        "closure_deps": "js/closure-dependencies.js",
        "files": ["js/config.js"] + JS_WIDGETIZER,
        "extra_defines": {"unisubs.REPORT_ANALYTICS": "false"},
        "bootloader": { 
            "template": "widget/widgetizerbootloader.js",
            "gatekeeper": "UnisubsWidgetizerLoaded",
            "render_bootloader": True
        }
    },
    "unisubs-widgetizer-debug": {
        "type": "js",
        "files": ["js/config.js" ] + JS_WIDGETIZER  ,
        "closure_deps": "js/closure-dependencies.js",
        "debug": True,
        "bootloader": { 
            "template": "widget/widgetizerbootloader.js",
            "gatekeeper": "UnisubsWidgetizerLoaded",
            "render_bootloader": True
        }
     },
    "unisubs-statwidget":{
        "type": "js",
        "closure_deps": "js/closure-stat-dependencies.js",
        "include_flash_deps": False,
        "files": [
            'js/unisubs.js',
            'js/rpc.js',
            'js/loadingdom.js',
            'js/statwidget/statwidgetconfig.js',
            'js/statwidget/statwidget.js'],
     },

    "unisubs-api":{
        "type": "js",
        "files": ["js/config.js"] + JS_API,
        "bootloader": { 
            "gatekeeper": "UnisubsApiLoaded", 
            "render_bootloader": False
        }
     },
    "js-base-dependencies":{
        "type":"js",
        "optimizations": "WHITESPACE_ONLY",
        "files": JS_BASE_DEPENDENCIES,
     },
    "js-onsite-dialog": {
        "type":"js",
        "files": ["js/config.js"]  + JS_DIALOG  ,
    },
    "site_base_js":{
        "type":"js",
        "optimizations": "WHITESPACE_ONLY",
        "files":[
              "js/jquery-1.4.3.js",
              "js/jquery-ui-1.8.16.custom.min.js",
              "js/jgrowl/jquery.jgrowl.js",
              "js/jalerts/jquery.alerts.js",
              "js/jquery.form.js",
              "js/jquery.metadata.js",
              "js/jquery.mod.js",
              "js/jquery.rpc.js",
              "js/jquery.input_replacement.min.js",
              "js/messages.js",
              "js/libs/chosen.jquery.min.js",
              "js/libs/chosen.ajax.jquery.js",
            ],
        "closure_deps": "",
        "include_flash_deps": False,
        },
    "js-jqueryui-datepicker":{
        "type":"js",
        "optimizations": "WHITESPACE_ONLY",
        "files":[
              "js/jquery-ui-1.8.16.custom.datepicker.min.js",
            ],
        "include_js_base_dependencies": False,
        },
    "js-testing-base":{
        "type":"js",
        "files": [
                 'js/widget/testing/stubvideoplayer.js',
                 'js/widget/testing/events.js',
                "js/subtracker.js" ,
                "js/unitofwork.js",
                "js/testing/testing.js",
                "js/testing/timerstub.js",
            ]
    },
    "css-teams-settings-panel":{
        "type":"css",
        "files":(
            "css/chosen.css",
            "css/unisubs-widget.css",
         ),
    },
    "js-teams":{
        "type":"js",
        "optimizations": "WHITESPACE_ONLY",
        "closure_deps": "",
        "files": (
            "js/libs/ICanHaz.js",
            "js/libs/classy.js",
            "js/libs/underscore.js",
            "js/libs/chosen.jquery.min.js",
            "js/libs/chosen.ajax.jquery.js",
            "js/jquery.mod.js",
            "js/teams/create-task.js",
         ),
        "include_js_base_dependencies": False,
        "include_flash_deps": False,
    },
    "debug-embed-js": {
        "type": "js",
        "optimizations": "WHITESPACE_ONLY",
        "files": JS_BASE_DEPENDENCIES + JS_OFFSITE[:-1]
    }
}


# this is used in our feature swither app, doorman, empty for now
FEATURE_FLAGS  = {
}

_INTEGRATION_PATH = os.path.join(PROJECT_ROOT, 'unisubs-integration')
_USE_INTEGRATION = os.path.exists(_INTEGRATION_PATH)
if _USE_INTEGRATION:
    sys.path.append(_INTEGRATION_PATH)

if _USE_INTEGRATION:
    for dirname in os.listdir(_INTEGRATION_PATH):
        if os.path.isfile(os.path.join(_INTEGRATION_PATH, dirname, '__init__.py')):
            INSTALLED_APPS += (dirname,)

EMAIL_BACKEND = "utils.safemail.InternalOnlyBackend"
EMAIL_FILE_PATH = '/tmp/unisubs-messages'
# on staging and dev only the emails listed bellow will receive actual mail
EMAIL_NOTIFICATION_RECEIVERS = ("arthur@stimuli.com.br", "steve@stevelosh.com", "@pculture.org")
# If True will not try to load media (e.g. javascript files) from third parties.
# If you're developing and have no net access, enable this setting on your
# settings_local.py
RUN_LOCALLY = False

try:
    import debug_toolbar

    EVERYONE_CAN_DEBUG = False
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.timer.TimerDebugPanel',
        # 'apps.testhelpers.debug_toolbar_extra.ProfilingPanel',
        # 'apps.testhelpers.debug_toolbar_extra.HaystackDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
    )

    def custom_show_toolbar(request):
        from django.conf import settings
        can_debug = settings.EVERYONE_CAN_DEBUG or request.user.is_staff

        if can_debug:
            if '__debug__/m/' in request.path or 'debug_toolbar' in request.GET:
                return True

        return False

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
        'EXTRA_SIGNALS': [],
        'HIDE_DJANGO_SQL': False,
        'TAG': 'div',
    }
except ImportError:
    pass
