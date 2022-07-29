
class User:
    def __init__(self, store, name):
        self.name = name
        self.store = store
        count = len(self.store['users']) + 1
        self.store['users'][count] = self
        self.id = count

    def viewings(self):
        views = list(self.store['viewings'].values())
        return [view for view in views if view.user.id == self.id]

    def find_viewings_for(self, episode):
        return [viewing for viewing in self.viewings() if viewing.episode == episode]

    def last_stop_time_for(self, episode):
        episode_viewings = self.find_viewings_for(episode)
        largest_stop_time = max([viewing.stop_time for viewing in episode_viewings])
        return largest_stop_time
                
    def episodes(self):
        return [viewing.episode for viewing in self.viewings()]
        