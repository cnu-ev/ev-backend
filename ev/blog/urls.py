from django.conf.urls import include, path, re_path
from . import views

app_name = blog

urlpatterns=[
    # / 의 경우
    path('',views.PostLV.as_view(), name='index'),

    # post/의 경우
    path('post/',views.PostLV.as_view(),name='post_list'),

    # 여기서부터는 정규식

    # /post/django-example/과 같은 slug를 가진 주소의 경우
    re_path('post/(?P<slug>[-\w]+)',views.PostDV.as_view(), name='post_detail'),

    #  /archive/
    re_path('archive/',views.PostAV.as_view(), name='post_archive'),

    # /2019/
    re_path('(?P<year>\d{4})',views.PostYAV.as_view(), name='post_year_archive'),

    # /2019/nov
    re_path('(?P<year>\d{4})/(?P<month<[a-z]{3}',views.PostMAV.as_view(), name='post_month_archive'),

    # /2019/nov/10
    re_path('(?P<year>\d{4})/(?P<month<[a-z]{3}/(?P<day>\d{1,2})',views.PostDAV.as_view(), name='post_day_archive'),

    # /today/
    re_path('today',views.PostTAV, name='post_today_archive'),

    

]