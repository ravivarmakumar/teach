class PynstaUser:

    def __init__(self, username):
        self.name = username
        self.friends = []   # A list of PynstaUsers
        self.posts = []     # A list of strings
        print('Created user', self.name)

    def add_friend(self, user):
        self.friends.append(user)
        print(self.name, 'added', user.get_username(), 'as a friend!')
        print('Your friend list looks like', self.get_friend_list())

    def post(self, message):
        self.posts.append(message)
        print(self.name, ' said, "', message, '"', sep='')

    def update_username(self, name):
        self.name = name
        print('Your username has been updated to', self.name)

    ### Getters ###

    def get_username(self):
        return self.name

    def get_friend_list(self):
        friends_str = '['
        for friend in self.friends:
            friends_str += friend.get_username() + ' '
        friends_str = friends_str.strip() + ']'
        return friends_str


def main():
    ravi = PynstaUser('rv')
    bhanu = PynstaUser('bp')
    vishnu = PynstaUser('vv')
    ravi.add_friend(bhanu)
    ravi.add_friend(vishnu)
    ravi.post('I made new friends!')
    ravi.update_username('rv008')

    # Next time: How can we make friendships go both ways?
    # i.e. If ravi adds bhanu as a friend, ravi should also be in bhanus friend list.


if __name__ == '__main__':
    main()
