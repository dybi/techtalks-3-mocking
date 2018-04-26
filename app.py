from api import PejsbookApi


class App(object):
    def __init__(self, api: PejsbookApi):
        self.api = api

    def poke_a_friend(self, friend_name):
        if self.api.check_user_status(friend_name) == 'active':
            self.api.send_private_message(friend_name, "Fancy a beer?", 0)
        elif self.api.check_user_status(friend_name) == 'inactive':
            self.api.post_to_friends_wall(friend_name, "We miss you!111")


if __name__ == '__main__':
    api = PejsbookApi()
    apka = App(api)
    apka.poke_a_friend("Ryan Gosling")