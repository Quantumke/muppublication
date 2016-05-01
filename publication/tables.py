import django_tables2 as tables
from .models import *
class adstable(tables.Table):
    class Meta:
        model=news_posts