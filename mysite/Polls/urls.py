from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),

    url(r'^login/$', views.Login , name = 'login'),

    url(r'^logout/$', views.Logout , name = 'logout'),

    url(r'^home/$', views.home , name = 'home'),

    url(r'^Blog/$', views.Blog, name = 'Blog'),

    url(r'^Register/$', views.register_user, name = 'register'),

    url(r'^Register_Success/$', views.register_Success, name = 'register_Success'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]