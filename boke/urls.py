'''自定义错误返回页面'''
from app01 import views as blog_views
from app01.feed import LatestEntriesFeed
from app01 import views as blog_view
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from app01.models import Entry


info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}
urlpatterns = [

    re_path(r'^login/', blog_view.login),  # 登录
    re_path(r'^logout/', blog_view.logout),  # 注销
    re_path(r'^latest/feed/', LatestEntriesFeed()),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^reply/(?P<comment_id>\d+)/$', blog_view.reply, name='comment_reply'),
    re_path(r'^admin/', admin.site.urls),
    re_path('^blog/', include('app01.urls')),
    path(r'',blog_view.index,name='index'),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
      name='django.contrib.sitemaps.views.sitemap'),
    # 添加图片
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error