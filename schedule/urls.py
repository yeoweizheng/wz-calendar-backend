from django.urls import path
from schedule.views import ScheduleItemListCreate, ScheduleItemRetrieveUpdateDestroy, TagListCreate, TagRetrieveUpdateDestroy

url_patterns = [
    path('schedule_items/', ScheduleItemListCreate.as_view()),
    path('schedule_items/<int:id>/', ScheduleItemRetrieveUpdateDestroy.as_view()),
    path('tags/', TagListCreate.as_view()),
    path('tags/<int:id>/', TagRetrieveUpdateDestroy.as_view()),
]
