from src.index import build_store
store = build_store()
class Viewing:
    def __init__(self, store, user, episode):
        self.user = user
        self.user_id = user.id
        self.episode = episode
        self.episode_id = episode.id
        self.episode_title = episode.title
        self.start_time = 0
        self.stop_time = ''
        self.id = len(store['viewings']) + 1
        store['viewings'].append(self)

    def words(self):
        word_list = self.episode.script.split()
        word_index = (self.stop_time) * 2.5
        return word_list[:100]

    def script(self):
        word_list = self.episode.script.split()
        word_index = (self.stop_time) * 2.5
        words = word_list[:100]
        return ' '.join(words)
