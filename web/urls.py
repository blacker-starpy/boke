from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app01.feed import LatestEntriesFeed
from app01 import views as blog_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from app01.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('app01.urls') ),
    url(r'^latest/feed/$', LatestEntriesFeed()),    #RSS订阅
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
      name='django.contrib.sitemaps.views.sitemap'),       #站点地图
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )        #添加图片的url

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error