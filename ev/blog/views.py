from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.vies.generic.dates import ArchiveIndexView, YearArchiveView,MonthArchiveView
from django.views.getneric.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    conetx_object_name = 'posts'
    paginate_by = 2

# DetailView
class PostDV(DetailView):
    model = Post

# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'