import sys
import time
from src.viewing import Viewing
class NetflixPlayer:
    def play_viewing(self, viewing):
        for letter in viewing.script():
            sys.stdout.write(letter)
            time.sleep(.0001)
        # https://stackoverflow.com/questions/8359317/pausing-the-python-console

    def play_episode_for(self, store, user, episode):
        last_stop_time = user.last_stop_time_for(episode)
        viewing = Viewing(store, user, episode)
        episode_end_time = episode.end_time()
        viewing.start_time = last_stop_time
        viewing.stop_time = episode_end_time
        
    def pause(self):
        pass