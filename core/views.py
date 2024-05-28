from django.shortcuts import render
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'core/group_list.html', {'groups': groups})
