from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.post_list,name='post_list'),
    url(r'^(?P<post_pk>\d+)/comment/create/$',views.createcomment,name='comment_create'),
]   