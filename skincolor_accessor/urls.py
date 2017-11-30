from django.conf.urls import url
from . import views

#creating a namespace so that views by the same name can be kept in multiple apps
app_name = 'skincolor_accessor'

urlpatterns = [
    # /skincolor_accessor/
    url(r'^$', views.index, name='index'),

    # /skincolor_accessor/id_no/
    url(r'^(?P<skintone_id>[0-9]+)/$', views.detail, name='detail'),
]
