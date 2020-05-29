from django.contrib.syndication.views import Feed
from .models import Entry

'''订阅功能'''
class LatestEntriesFeed(Feed):
    title = 'star 的博客'
    link = '/siteblogs/'

    description_template = 'star 的最新博客'


    def items(self):
        '''展示最新的5篇博客'''
        return Entry.objects.order_by('-create_time')[:5]
    def item_title(self,item):
        return item.title

    def item_description(self, item):
        '''摘要'''
        return item.abstract

