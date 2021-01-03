from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.insta,name='insta'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^post(?P<post_id>\d+)', views.single_post, name='single_post'),
    url(r'^follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)