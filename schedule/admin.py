from django.contrib import admin
from schedule.models import ScheduleItem

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'done')
    list_filter = ('user', )


admin.site.register(ScheduleItem, ScheduleItemAdmin)