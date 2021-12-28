from django.urls import path
from schedule.views import ScheduleItemListCreate

url_patterns = [
    path('schedule_items/', ScheduleItemListCreate.as_view()),
]
