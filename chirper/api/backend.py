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

    def _parse_hashtags(self, hashtags):
        return [hashtag.text for hashtag in hashtags]

    def _parse_tweets(self, tweets):
        response = []
        for tweet in tweets:
            user = tweet.user
            hashtags = self._parse_hashtags(tweet.hashtags)
            data = {
                'account': {
                    'fullname': user.name,
                    'id': user.id,
                    'url': user.url,
                },
                'date': tweet.created_at,
                'hashtags': hashtags,
                'retweets': tweet.retweet_count,
                'text': tweet.text,
                'favorites': tweet.favorite_count
            }
            response.append(data)
        return response

    def _verify_credentials(self):
        return self.twitter.VerifyCredentials()

    def get_user_tweets(self, screen_name, count=30):
        tweets = self.twitter.GetUserTimeline(
            screen_name='@{}'.format(screen_name),
            count=count,
        )

        return self._parse_tweets(tweets)

    def get_tweets_by_hashtags(self, hashtag, count=30):
        tweets = self.twitter.GetSearch(
            term='#{}'.format(hashtag),
            count=count,
        )

        return self._parse_tweets(tweets)