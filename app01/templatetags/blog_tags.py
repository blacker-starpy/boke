from django import template
from app01.models import Entry,Category,Tag

register = template.Library()

'''博客侧边栏'''
@register.simple_tag
def get_recent_entries(num=5):
    '''倒叙排列'''
    return Entry.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_popular_entries(num=5):
    '''访问量排序'''
    return Entry.objects.all().order_by('-visiting')[:num]

@register.simple_tag
def get_categories():
    '''博客分类'''
    return Category.objects.all()

@register.simple_tag
def get_entry_count_of_category(category_name):
    '''标签'''
    return Entry.objects.filter(category__name= category_name).count

@register.simple_tag
def archives():
    '''当前月份的博客'''
    return Entry.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_entry_count_of_date(year, month):
    '''往年的/望月的'''
    return Entry.objects.filter(created_time__year=year, created_time__month=month).count()

@register.simple_tag
def get_tags():
    '''标签云'''
    return Tag.objects.all()