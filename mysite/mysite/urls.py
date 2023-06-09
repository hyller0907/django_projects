import os
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path, re_path
from django.views.static import serve

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('admin/', admin.site.urls),
    re_path(r'^site/(?P<path>.*)$', serve, {'document_root': SITE_ROOT, 'show_indexes':True}, name='site_path'),

    # Applications
    path('polls/', include('polls.urls')),
    path('hello/', include('hello.urls')),
]