from django.db import models
from django.core.exceptions import ValidationError


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        if self.student_set.count() > 10:
            raise ValidationError('A group can have a maximum of 10 students.')


class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.group and self.group.student_set.count() >= 10:
            raise ValidationError('This group already has 10 students.')
        super().save(*args, **kwargs)
