from django.urls import path
from schedule.views import ScheduleItemListCreate, ScheduleItemRetrieveUpdateDestroy

url_patterns = [
    path('schedule_items/', ScheduleItemListCreate.as_view()),
    path('schedule_items/<int:id>/', ScheduleItemRetrieveUpdateDestroy.as_view()),
]
