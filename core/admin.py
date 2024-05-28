from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Student, Group


class StudentForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')
        if group and group.student_set.count() >= 10:
            raise ValidationError('This group already has 10 students.')
        return cleaned_data


class StudentAdmin(admin.ModelAdmin):
    form = StudentForm


admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
