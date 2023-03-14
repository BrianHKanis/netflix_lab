from src.index import build_store
class Episode:
    def __init__(self, store, title):
        self.store = store
        self.title = title
        self.id = len(store['episodes']) + 1
        store['episodes'][self.id] = self
        self.script = open('./data/seinfeld/1-01-good-news-bad-news/script.txt', 'r').read()

    def words(self):
        return self.script.split()
    
    def viewings(self):
        return [viewing for viewing in self.store['viewings'] if viewing.episode_id == self.id]
    
    def users(self):
        return self.store['users']
    
    def end_time(self):
        return len(self.script.split()) * 2.5 