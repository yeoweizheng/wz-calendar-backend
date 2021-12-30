from django.contrib import admin
from schedule.models import ScheduleItem
from rangefilter.filters import DateRangeFilter

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'done')
    list_filter = ('user', ('date', DateRangeFilter), 'done')
    search_fields = ('name',)

    def get_rangefilter_date_title(self, request, field_path):
        return 'By date'


admin.site.register(ScheduleItem, ScheduleItemAdmin)