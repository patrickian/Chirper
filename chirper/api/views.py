from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.backend import Twitter

class HashtagTweetListAPIView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, hashtag):
        twitter = Twitter()

        return Response(twitter.get_tweets_by_hashtags(hashtag))


class UserTweetListAPIView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, user):
        twitter = Twitter()
        
        return Response(twitter.get_user_tweets(user))