from decouple import config
import tweepy


class TwitterBot:

    """ Class responsible to receive and send messages using Twitter

    Usage Example:
        bot = TwitterBot()
        bot.send_text('hello world')

    """

    def __init__(self: object) -> None:
        auth = tweepy.OAuthHandler(
            config('twitter_consumer_key'),
            config('twitter_consumer_secret')
        )

        auth.set_access_token(
            config('twitter_access_token'),
            config('twitter_access_token_secret')
        )

        self.api = tweepy.API(auth)

    def send_media(self: object, media: str, message: str) -> None:
        """ Send the image and a message to Twitter account 
        """
        self.api.update_with_media(media, message)

    def send_text(self: object, message: str) -> None:
        """ Send a message to Twitter account 
        """
        self.api.update_status(message)
