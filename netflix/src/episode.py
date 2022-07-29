import sys
import time

class Episode:
    def __init__(self, store, title):
        self.title = title
        self.store = store
        count = len(self.store['episodes']) + 1
        self.store['episodes'][count] = self
        self.id = count

    def words(self):
        return [word for word in self.script.split(' ') if word and word != '\n']

    def end_time(self):
        return len(self.words()) * 2.5

    def viewings(self):
        return [viewing for viewing in self.store['viewings'].values() if viewing.episode == self]

    def users(self):
        return [viewing.user for viewing in self.viewings()]

    def play_script(self):
        for letter in self.script:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.02)


    