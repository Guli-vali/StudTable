from django.conf.urls import url

from ..views import (DetailStudent, CreateStudent,
        StudentUpdate, StudentDelete)


urlpatterns = [
    url(r'^create/$',
        CreateStudent.as_view(),
        name='datatable_student_create'),
    url(r'^(?P<id>\d+)/$',
        DetailStudent.as_view(),
        name='datatable_student_detail'
        ),
    url(r'^(?P<id>\d+)/delete/',
        StudentDelete.as_view(),
        name='datatable_student_delete'),
    url(r'^(?P<id>\d+)/update/',
        StudentUpdate.as_view(),
        name='datatable_student_update'),
]