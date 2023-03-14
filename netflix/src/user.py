from src.index import build_store
class User:
    def __init__(self, store, name):
        self.name = name
        self.store = store
        self.id = len(store['users']) + 1
        store['users'].append(self)

    def viewings(self):
        return [viewing for viewing in self.store['viewings'] if viewing.user_id == self.id]
    
    def episodes(self):
        return [viewing.episode for viewing in self.store['viewings'] if viewing.user_id == self.id]
    
    def find_viewings_for(self, episode):
        return [viewing for viewing in self.store['viewings'] if viewing.episode == episode]
    
    def last_stop_time_for(self, episode):
        recent_viewings = [viewing for viewing in self.store['viewings'] if viewing.episode == episode]
        return recent_viewings[-1].stop_time