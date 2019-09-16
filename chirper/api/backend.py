import twitter

from django.conf import settings


class Twitter(object):
    """
    Backend Class for Twitter API.
    Handles basic requests for tweets based from
    user and hashtags and parsing of tweets.
    """
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
        """
        Parse Hashtag objects and returns list of hashtags as text.
        """
        return [hashtag.text for hashtag in hashtags]

    def _parse_tweets(self, tweets):
        """
        Returns a list of tweets parsed as dictionary.
        :example:
        [
            {
                "favorites": 68,
                "account": {
                    "fullname": "John Doe",
                    "url": "https://ti.co/onlysample",
                    "id": 123123123
                },
                "date": "Mon Sep 14 08:09:03 +0000 2019",
                "text": "Sample tweeeeeeeet!!!",
                "hashtags": [
                    "Python"
                ],
                "retweets": 40
            }
        ]
        """
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
        """Verify credentials and returns User object."""
        return self.twitter.VerifyCredentials()

    def get_user_tweets(self, screen_name, count=30):
        """
        Retrieves user based tweets.Returns a list of tweets.
        """
        tweets = self.twitter.GetUserTimeline(
            screen_name='@{}'.format(screen_name),
            count=count,
        )

        return self._parse_tweets(tweets)

    def get_tweets_by_hashtags(self, hashtag, count=30):
        """
        Retrieves hashtag based tweets.Returns a list of tweets.
        """
        tweets = self.twitter.GetSearch(
            term='#{}'.format(hashtag),
            count=count,
        )

        return self._parse_tweets(tweets)