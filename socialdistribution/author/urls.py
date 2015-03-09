from django.conf.urls import patterns, url

from author import views

urlpatterns = patterns(
    'author.views',

    url(r'^$', 'login', name='login'),
    url(r'^register/$', 'register', name='register'),
    url(r'^author/logout/$', views.logout),
    url(r'^author/(?P<author>\d+)/$', views.profile),
    url(r'^author/search/$', views.search),
    #url(r'^author/(?P<author>\d+)/posts/$', views.other),
    url(r'^author/friends/new$', views.request_friendship, name='request_friendship'),
    url(r'^author/(?P<author>\d+)/FriendRequests$', views.friend_request_list, name = 'friend_request_list'),
)
