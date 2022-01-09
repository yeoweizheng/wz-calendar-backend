from django.db.models import query
from rest_framework import generics
from rest_framework.utils import serializer_helpers
from schedule.models import ScheduleItem, Tag
from schedule.serializers import ScheduleItemSerializer, TagSerializer
from wzcalendar.mixins import BaseViewMixin

class ScheduleItemListCreate(BaseViewMixin, generics.ListCreateAPIView):

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        tag = self.request.query_params.get('tag')
        queryset = ScheduleItem.objects.filter(user=self.request.user)
        if start_date and end_date:
            queryset = queryset.filter(date__gte=start_date, date__lte=end_date)
        if tag:
            if tag == 'u':
                queryset = queryset.filter(tag=None)
            else:
                queryset = queryset.filter(tag=tag)
        return queryset

    serializer_class = ScheduleItemSerializer


class ScheduleItemRetrieveUpdateDestroy(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return ScheduleItem.objects.filter(user=self.request.user)
    
    serializer_class = ScheduleItemSerializer


class TagListCreate(BaseViewMixin, generics.ListCreateAPIView):

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user).order_by('name')
    
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroy(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        ScheduleItem.objects.filter(tag__id=kwargs['id']).update(tag=None)
        return super().destroy(request, *args, **kwargs)

    serializer_class = TagSerializer