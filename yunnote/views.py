from django_filters.filters import OrderingFilter
from rest_framework import viewsets, filters
from yunnote.util.customModelViewSet import CustomModelViewSet
from yunnote.models import Group, Note
from yunnote.serializers import GroupSerializer, NoteSerializer
from yunnote.filter import GroupFilter, NoteFilter
from django_filters import rest_framework

# Create your views here.


class GroupViewSet(CustomModelViewSet, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'
    filter_backends = (rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter)
    filter_class = GroupFilter
    ordering_fields = ['sort_no']
    ordering = 'sort_no'


class NoteViewSet(CustomModelViewSet, viewsets.GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
    filter_backends = (rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter)
    filter_class = NoteFilter
    ordering_fields = ['sort_no']
    ordering = 'sort_no'
