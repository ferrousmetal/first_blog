from django.urls import path
from comments.views import *

app_name = 'comments'

urlpatterns = [
    path(r'^comment/post/(?P<post_pk>[0-9]+)/$', post_comment, name='post_comment'),

]
