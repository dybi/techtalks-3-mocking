# define authentication credentials
from random import choice

CONSUMER_KEY = 'iYD2sKY4NC8teRb9BUM8UguRa'
CONSUMER_SECRET = 'uW3tHdH6UAqlxA7yxmcr8FSMSzQIBIpcC4NNS7jrvkxREdJ15m'
ACCESS_TOKE_KEY = '314746354-Ucq36TRDnfGAxpOVtnK1qZxMfRKzFHFhyRqzNpTx7wZ1qHS0qycy0aNjoMDpKhcfzuLm6uAbhB2LilxZzST8w'
ACCESS_TOKEN_SECRET = '7wZ1qHS0qycy0aNjoMDpKhcfzuLm6uAbhB2LilxZzST8w'


class PejsbookApi(object):
    def __init__(
            self,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token_key=ACCESS_TOKE_KEY,
            access_token_secret=ACCESS_TOKEN_SECRET
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

    def post_to_a_wall(self, msg):
        pass

    def post_to_friends_wall(self, user_name, msg):
        return True

    def send_private_message(self, user_name, msg, timeout):
        return True

    def check_user_status(self, user_name):
        if self._is_friend(user_name):
            status = ["active", "inactive"]
            return choice(status)
        return "unkown"

    def update_profile_picture(self, picture):
        pass

    def invite_user(self, user_name):
        pass

    def _is_friend(self, user_name):
        return user_name == "Ryan Gosling"

