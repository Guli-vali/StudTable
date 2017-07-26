from django import forms
from .models import Student, StudyGroup
from django.forms.widgets import HiddenInput


class GroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = '__all__'
        widgets = {'slug': HiddenInput()}

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        return new_slug

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'