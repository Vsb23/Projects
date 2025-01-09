import os 
import psutil
import random
from pathlib import Path
import subprocess
import mpv
import time

animes = os.listdir('series')


with os.scandir('series') as series:
    list_ser = list(series)
    for i in range(5):
        anime = random.choice(list_ser)
        print(anime.name)
        with os.scandir(anime) as episodes:
            list_ep = list(episodes)
            max_episodes = min(len(list_ep), 5) #serve per evitare che il 
            for i in range(random.randint(1, max_episodes)):
                f = open("playlist.txt", "a")
                f.write('series/' + str(anime.name) + "/" + str(list_ep[i].name) + "\n")
                f.close()
                print("scritto file")

p = Path('playlist.txt')
p.rename(p.with_suffix('.m3u'))



player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True)
player.loadlist('playlist.m3u', mode='replace')
player.command("playlist-play-index", 0)
try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("Closing MPV...")
  player.terminate()