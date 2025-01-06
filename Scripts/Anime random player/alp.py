import os 
import psutil
import random
from pathlib import Path


animes = os.listdir('series')

mpv = [item.pid for item in psutil.process_iter() if item.name() == 'mpv.exe']



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
os.system('mpv --playlist=playlist.m3u')

