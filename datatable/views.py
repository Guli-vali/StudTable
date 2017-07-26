from user.decorators import (
    class_login_required,
    require_authenticated_permission)

from django.views.generic import ListView, CreateView,\
    UpdateView, DeleteView, DetailView

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from .models import StudyGroup, Student
from .forms import GroupForm, StudentForm


class GroupList(ListView):
    model = StudyGroup
    context_object_name = 'groups'


@require_authenticated_permission(
    'datatable.add_studygroup')
class CreateGroup(CreateView):
    form_class = GroupForm
    model = StudyGroup

    def get_success_url(self):
        return self.object.get_absolute_url()


@require_authenticated_permission(
    'datatable.change_studygroup')
class GroupUpdate(UpdateView):
    form_class = GroupForm
    model = StudyGroup

    success_url = reverse_lazy(
        'grouptable_group_list')


@require_authenticated_permission(
    'datatable.delete_studygroup')
class GroupDelete(DeleteView):
    model = StudyGroup

    success_url = reverse_lazy(
        'grouptable_group_list')


@class_login_required
class StudentList(ListView):
    context_object_name = 'students'

    def get_queryset(self):
        self.studygroup = get_object_or_404(
            StudyGroup, slug=self.kwargs['slug'])
        return Student.objects.filter(studygroup=self.studygroup)

    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)

        context['title'] = self.kwargs['slug']
        return context


@require_authenticated_permission(
    'datatable.add_student')
class CreateStudent(CreateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return self.object.studygroup.get_absolute_url()


@class_login_required
class DetailStudent(DetailView):
    model = Student

    def get_object(self, queryset=None):
        self.student = get_object_or_404(
                    Student, id=self.kwargs['id'])
        return self.student


@require_authenticated_permission(
    'datatable.change_student')
class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student

    def get_object(self, queryset=None):
        self.student = get_object_or_404(
                    Student, id=self.kwargs['id'])
        return self.student

    def get_success_url(self):
        return self.object.studygroup.get_absolute_url()


@require_authenticated_permission(
    'datatable.delete_student')
class StudentDelete(DeleteView):
    model = Student

    def get_object(self, queryset=None):
        self.student = get_object_or_404(
                    Student, id=self.kwargs['id'])
        return self.student

    def get_success_url(self):
        return self.object.studygroup.get_absolute_url()
