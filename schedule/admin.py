from django.contrib import admin
from schedule.models import ScheduleItem
from rangefilter.filters import DateRangeFilter

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'done')
    list_filter = ('user', ('date', DateRangeFilter), 'done')


admin.site.register(ScheduleItem, ScheduleItemAdmin)