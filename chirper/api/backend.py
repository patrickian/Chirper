import requests

from requests_oauthlib import OAuth1
from urllib.parse import urlencode

from django.conf import settings


class Twitter(object):
    """
    Backend Class for Twitter API.
    Handles basic requests for tweets based from
    user and hashtags and parsing of tweets.
    """

    BASE_URL = 'https://api.twitter.com/1.1'
    SEARCH_PATH_URL = '/search/tweets.json'
    USER_PATH_URL = '/statuses/user_timeline.json'

    def __init__(self):
        self.__session = requests.Session()
        self.__auth = OAuth1(
            settings.TWITTER_CONSUMER_KEY,
            settings.TWITTER_CONSUMER_SECRET,
            settings.TWITTER_ACCESS_TOKEN_KEY,
            settings.TWITTER_ACCESS_TOKEN_SECRET,
        )

    def get_user_tweets(self, screen_name, count=30):
        """
        Retrieves user based tweets.Returns a list of tweets.
        """
        parameters = {
            'screen_name': '@{}'.format(screen_name),
            'count': count
        }

        return self._retrieve_tweets(self.USER_PATH_URL, parameters)

    def get_tweets_by_hashtags(self, hashtag, count=30):
        """
        Retrieves hashtag based tweets.Returns a list of tweets.
        """
        parameters = {
            'q': '#{}'.format(hashtag),
            'count': count
        }

        return self._retrieve_tweets(self.SEARCH_PATH_URL, parameters)

    def _parse_response_hashtags(self, hashtags):
        """
        Parse Hashtag objects and returns list of hashtags as text.
        """
        return [hashtag['text'] for hashtag in hashtags]

    def _parse_response_tweets(self, tweets):
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
            user = tweet['user']
            hashtags = tweet['entities']['hashtags']
            data = {
                'favorites': tweet['favorite_count'],
                'account': {
                    'fullname': user['name'],
                    'href': '/{}'.format(user['screen_name']),
                    'id': user['id']
                },
                'date': tweet['created_at'],
                'text': tweet['text'],
                'hashtags': self._parse_response_hashtags(hashtags),
                'retweets': tweet['retweet_count']
            }
            response.append(data)
    
        return response

    def _retrieve_tweets(self, path, parameters):
        """
        Generic request for requesting tweets in Twitter API.
        Returns a parsed list for tweets.
        """
        url = '{}{}?{}'.format(
            self.BASE_URL,
            path,
            urlencode(parameters)
        )
        response = self.__session.get(url, auth=self.__auth)

        if response.status_code != 200:
            response.raise_for_status()

        tweets = response.json()
        if isinstance(tweets, dict):
            tweets = data['statuses']

        return self._parse_response_tweets(tweets)
