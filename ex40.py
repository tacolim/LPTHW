class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday2 = Song(["Happy, Happy Birthday",
                    "From all of us to you",
                    "We wish it was our birthday",
                    "So we could party too",
                    "Yay!",
                    "Ho! ho! Ho! It's your birthday?!"])

happy_bday.sing_me_a_song()
print '-' * 10
bulls_on_parade.sing_me_a_song()
print '-' * 10
happy_bday2.sing_me_a_song()
