from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.insta,name='insta'),
    url(r'^accounts/profile/', views.insta, name='insta'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^delete/post/(?P<post_id>\d+)',views.delete_post,name = 'delete_post'),
    url(r'^update/post/(?P<post_id>\d+)',views.update_post,name = 'update_post'),
    url(r'^add/profile/$',views.add_profile,name = 'add_profile'),
    url(r'^my_profile/$',views.my_profile,name = 'my_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^post(?P<post_id>\d+)', views.single_post, name='single_post'),
    url(r'^follow/(\d+)',views.follow,name = 'follow'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)