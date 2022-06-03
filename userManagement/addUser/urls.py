from django.conf.urls import url
from django.urls import path, include
from .views import (
    UserListView,
)

#create endpoint
urlpatterns = [
    path('add', UserListView.as_view()),
]
