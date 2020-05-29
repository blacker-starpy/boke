from app01.feed import LatestEntriesFeed
from app01 import views as blog_view
from django.urls import path,re_path,include

urlpatterns = [
    re_path(r'^login/',blog_view.login),     #登录
    re_path(r'^logout/',blog_view.logout),   #注销
    re_path(r'^latest/feed/',LatestEntriesFeed()),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^reply/(?P<comment_id>\d+)/$', blog_view.reply, name='comment_reply'),

]

'''自定义错误返回页面'''
from app01 import views as blog_views

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error
