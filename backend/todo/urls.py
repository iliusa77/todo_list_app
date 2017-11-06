#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'tasks', views.TaskViewSet)
#router.register(r'grouptask', views.GroupTaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tasks/$', views.TaskListView.as_view()),
    url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view()),
    url(r'^grouptasks/$', views.GroupListView.as_view()),
    url(r'^grouptasks/(?P<pk>\d+)/$', views.GroupListDetailView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
