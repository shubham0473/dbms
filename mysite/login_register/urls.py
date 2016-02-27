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

    url(r'^$', views.Login, name = 'login'),
    ]