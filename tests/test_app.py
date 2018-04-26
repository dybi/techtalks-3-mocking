from unittest import TestCase, expectedFailure
from unittest.mock import create_autospec

from api import PejsbookApi
from app import App


class TestApp(TestCase):
    def test_that_poking_a_friend_sends_a_private_message_when_friend_is_active(self):
        api = create_autospec(spec=PejsbookApi)
        api.check_user_status.return_value = 'active'
        app = App(api)
        friend = "Ryan Gosling"
        app.poke_a_friend(friend)
        api.check_user_status.assert_called_once_with(friend)
        api.send_private_message.assert_called_once_with(friend, "Fancy a beer?")

    @expectedFailure
    def test_that_poking_a_friend_posts_to_a_friends_wall_when_friend_is__inactive(self):
        self.fail()

    @expectedFailure
    def test_that_poking_neither_posts_to_a_wall_nor_sendS_private_message_when_poking_stranger(self):
        self.fail()
