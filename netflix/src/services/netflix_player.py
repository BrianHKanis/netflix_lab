import sys
from src.viewing import Viewing
class NetflixPlayer:
    def __init__(self):
        pass


    def play_viewing(self, viewing):
        script = viewing.episode.words()
        for i in range(int(2.5*(viewing.start_time)), int(2.5*(viewing.stop_time))):
            sys.stdout.write(script[i])
            sys.stdout.write(" ")
            sys.stdout.flush()
            #time.sleep(0.4)
            print("")

    def play_episode_for(self, store, user, episode):
        viewings = [viewing for viewing in episode.viewings() if viewing.user.id == user.id and viewing.episode_id == episode.id]
        last_stop = viewings[-1].stop_time
        new_view = Viewing(store, user, episode)
        new_view.start_time = last_stop