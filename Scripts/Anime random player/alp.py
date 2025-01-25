import os 
import psutil
import random
from pathlib import Path
import subprocess
import mpv
import threading


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


cond = threading.Condition()
key = None	

player = mpv.MPV(
    input_default_bindings=False,
    input_vo_keyboard = True,
    terminal=True,
    input_terminal=True,
    osc=True
)

def wait_key(player: mpv.MPV) -> str:
	
	cond = threading.Condition()
	key = None
	
	@player.on_key_press("q")
	def on_q():
		nonlocal key
		key = 'q'
		with cond:
			cond.notify()
	
	@player.on_key_press("<")
	def on_prev():
		nonlocal key
		key = '<'
		with cond:
			cond.notify()
	
	
	@player.on_key_press(">")
	def on_next():
		nonlocal key
		key = '>'
		with cond:
			cond.notify()
	
	with cond:
		cond.wait(timeout=None)
	on_q.unregister_mpv_key_bindings()
	on_next.unregister_mpv_key_bindings()
	on_prev.unregister_mpv_key_bindings()
	
	return key

try:
    player.loadlist('playlist.m3u', mode='replace')
    player.command("playlist-play-index", 0)
    player.wait_until_playing()
    keypressed = wait_key(player)
    input(f"hai premuto {keypressed}")
except Exception as e:
	pass
finally:
	player.terminate()