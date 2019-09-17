from django.test import TestCase
from .backend import Twitter


class TwitterTestCase(TestCase):

    def test_retrieving_tweets_using_screen_name(self):
        """
        Pulling of tweets based on user. Backend should be able
        to retrieve tweets of the correct user.
        """
        NAME = 'Patrick Concepcion'
        twitter = Twitter()
        tweets = twitter.get_user_tweets('ptrckcncpcn')

        if not tweets:
            self.fail('No tweets pulled.')

        for tweet in tweets:
            self.assertEqual(tweet['account']['fullname'], NAME)