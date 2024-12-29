import os 
import psutil
import random
animes = os.listdir('series')

mpv = [item.pid for item in psutil.process_iter() if item.name() == 'mpv.exe']



with os.scandir('series') as series:
    anime = random.choice(list(series))
    episode = os.listdir(anime.path)
    print(f'Now watching: {anime.name} episode: {episode[0]}')
    os.system(f'mpv series/"{anime.name}/{episode[0]}"')
    while mpv == []:
        os.remove(f"series/{anime.name}/{episode[0]}")
        print(f"Eliminato il file {episode[0]} di {anime.name}")

