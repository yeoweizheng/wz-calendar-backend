from django.contrib import admin
from schedule.models import ScheduleItem, Tag
from rangefilter.filters import DateRangeFilter

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'done', 'tag', 'user')
    list_filter = ('user', ('date', DateRangeFilter), 'done', 'tag')
    search_fields = ('name',)
    ordering = ('date',)

    def get_rangefilter_date_title(self, request, field_path):
        return 'By date'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


admin.site.register(ScheduleItem, ScheduleItemAdmin)
admin.site.register(Tag, TagAdmin)