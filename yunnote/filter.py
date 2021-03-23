from django.db import models
import django_filters
from yunnote.models import Group, Note


class GroupFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='startswith')

    class Meta:
        model = Group
        fields = ['id', 'name']


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = ['id', 'name', 'group_id']
