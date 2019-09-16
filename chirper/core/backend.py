import twitter

from django.conf import settings


class Twitter(object):

    def __init__(self):
        self.twitter = twitter.Api(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET,
        )
        # Verify credentials
        self.__user = self._verify_credentials()

    def _verify_credentials(self):
        return self.twitter.VerifyCredentials()

    def get_user_tweets(self, screen_name, count=30):
        return self.twitter.GetUserTimeline(
            screen_name=screen_name,
            count=count,
        )

    def get_tweets_by_hashtags(self, hashtag, count=30):
        return self.twitter.GetSearch(
            term=hashtag,
            count=count,
        )
