from django.urls import path
from .views import *

urlpatterns = [
    path("send-mail", EmailRequest.as_view()),
]
