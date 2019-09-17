from django.urls import path

from .views import HashtagTweetListAPIView
from .views import UserTweetListAPIView


urlpatterns = [
    path(
        'hashtags/<hashtag>/',
        HashtagTweetListAPIView.as_view(),
        name='hashtag'
    ),
    path(
        'users/<user>/',
        UserTweetListAPIView.as_view(),
        name='user'
    ),
]
