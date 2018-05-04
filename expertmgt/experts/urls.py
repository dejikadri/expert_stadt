from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^api/experts/$', views.ExpertList.as_view()),
    url(r'^api/experts/(?P<pk>[0-9]+)$', views.ExpertDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
