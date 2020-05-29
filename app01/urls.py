from django.urls import path,re_path,include

from . import views
app_name= 'app01'

urlpatterns = [
    re_path(r'^(?P<blog_id>[0-9]+)',views.detail,name='blog_detail'),
    re_path(r'^category/(?P<category_id>[0-9]+)/',views.catagory,name='blog_category'),  # 分类查询
    re_path(r'^tag/(?P<tag_id>[0-9]+)/',views.tag,name='blog_tag'),  # 分类查询
    re_path(r'^search/',views.search,name='blog_search'),  # 分类查询
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<mouth>[0-9]+)',views.archives,name='blog_archives'),  # 博客归档
    re_path(r'^reply/(?P<comment_id>\d+)/', views.reply, name='comment_reply'),    #评论回复
    re_path(r'^',views.index,name='index'),   # 注意： 默认匹配到了之后就不再匹配了 ！！！

]