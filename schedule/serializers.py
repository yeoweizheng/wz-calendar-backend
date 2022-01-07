from rest_framework import serializers
from schedule.models import ScheduleItem, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
    
    def save(self):
        return super().save(user=self.context['request'].user)


class ScheduleItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleItem
        fields = ('id', 'name', 'date', 'done')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'] = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.filter(user=self.context['request'].user), allow_null=True)
    
    def save(self):
        return super().save(user=self.context['request'].user)