from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
]