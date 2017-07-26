from django.conf.urls import url

from ..views import (GroupList, CreateGroup,
    GroupUpdate, StudentList, GroupDelete)

urlpatterns = [
    url(r'^$',
        GroupList.as_view(),
        name='grouptable_group_list'),
    url(r'^(?P<slug>[\w\-]+)$',
        StudentList.as_view(),
        name='grouptable_student_list'),
    url(r'^create/',
        CreateGroup.as_view(),
        name='datatable_group_create'),
    url(r'^(?P<slug>[\w\-]+)/delete/',
        GroupDelete.as_view(),
        name='datatable_group_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/',
        GroupUpdate.as_view(),
        name='datatable_group_update'),
]