from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class StudyGroup(models.Model):
    title = models.CharField(max_length=31)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        allow_unicode=True,
        blank=True)
    head = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        slug = '%s' % self.title
        self.slug = slugify(slug, allow_unicode=True)
        super(StudyGroup, self).save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse('grouptable_student_list',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('datatable_group_delete',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('datatable_group_update',
                       kwargs={'slug': self.slug})

    def stud_num(self):
        return self.students.count()


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    birthday = models.DateField()
    studygroup = models.ForeignKey(StudyGroup, related_name='students')


    def __str__(self):
        return self.full_names

    def get_absolute_url(self):
        return reverse('datatable_student_detail',
                       kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('datatable_student_update',
                       kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('datatable_student_delete',
                       kwargs={'id': self.id})

