from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken

url_patterns = [
    path('token/', ObtainJSONWebToken.as_view()),
]
