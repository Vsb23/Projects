import os 
import psutil
import random
animes = os.listdir('series')

mpv = [item.pid for item in psutil.process_iter() if item.name() == 'mpv.exe']



with os.scandir('series') as series:
    list_ser = list(series)
    for i in range(5):
        anime = random.choice(list_ser)
        print(anime.name)
        with os.scandir(anime) as episodes:
            list_ep = list(episodes)
            max_episodes = max(len(list_ep), 5) #serve per evitare che il 
            for i in range(random.randint(1, max_episodes)):
                f = open("playlist.txt", "a")
                f.write(str(anime.name) + "/" + str(list_ep[i].name) + "\n")
                f.close()
                print("scritto file")

