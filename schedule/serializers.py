from rest_framework import serializers
from schedule.models import ScheduleItem

class ScheduleItemSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleItem
        fields = ('id', 'name', 'details', 'date', 'attributes')
    
    def save(self):
        return super().save(user=self.context['request'].user)