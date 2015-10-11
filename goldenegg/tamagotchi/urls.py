from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tamagotchi/
    url(r'^$', views.index, name='index'),
    # ex: /tamagotchi/homepage/
    url(r'^/homepage/$', views.homepage, name='homepage'),
    # ex: /tamagotchi/choose/
    url(r'^/choose/$', views.choose, name='choose'),
    # ex: /tamagotchi/5/
    url(r'^(?P<user_id>[0-9]+)/$', views.user, name='user'),
    # ex: /tamagotchi/5/pet/
    url(r'^(?P<user_id>[0-9]+)/pet/$', views.pet, name='pet'),
]
