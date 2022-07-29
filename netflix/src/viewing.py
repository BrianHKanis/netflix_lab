
class Viewing:
    def __init__(self, store, user, episode):
        self.store = store
        self.user = user
        self.episode = episode
        self.user_id = user.id
        self.episode_id = episode.id
        count = len(self.store['viewings']) + 1
        self.store['viewings'][count] = self
        self.id = count

    def words(self):
        # needs to work for both beginning of episode and middle of episode
        start_word = int(self.start_time * 2.5)
        end_word = int(self.stop_time * 2.5)
        return self.episode.words()[start_word:end_word]

    def script(self):
        return ' '.join(self.words())
