from django.conf.urls import patterns, url
from test_app.views import get_users

urlpatterns = patterns('',
    url(r'^get_users/$', get_users, name='users'),
    url(r'^get_user/(?P<key>[0-9]+)/$', get_users, name='user'),
)
