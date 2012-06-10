from django.conf.urls import patterns, include, url

urlpatterns = patterns('posts.views',
    url(r'^index', 'index'),
    url(r'^(?P<post_id>\d+)$', 'details'),
    url(r'^(?P<post_id>\d+)/(?P<post_title>\w+)/', 'test'),
)