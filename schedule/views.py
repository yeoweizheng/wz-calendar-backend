from rest_framework import generics
from schedule.models import ScheduleItem
from schedule.serializers import ScheduleItemSeriallizer
from wzcalendar.mixins import BaseViewMixin

class ScheduleItemListCreate(BaseViewMixin, generics.ListCreateAPIView):

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            return ScheduleItem.objects.filter(user=self.request.user, date__gte=start_date, date__lte=end_date)
        else:
            return ScheduleItem.objects.filter(user=self.request.user)

    serializer_class = ScheduleItemSeriallizer


class ScheduleItemRetrieveUpdateDestroy(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return ScheduleItem.objects.filter(user=self.request.user)
    
    serializer_class = ScheduleItemSeriallizer