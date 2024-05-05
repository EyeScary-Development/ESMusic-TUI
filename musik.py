import time
import random
import asyncio
import sys 
import select
import os
import subprocess
from nava import play, stop
print("welcome to Musik")


async def menu(sound):
    rlist, _, _ = select.select([sys.stdin], [],[], 20)
    if rlist:
        usin=input()
        match usin:
            case "stop":
                stop(sound)
                return True
            case "skip":
                stop(sound)
                return False
            case "exit":
                exit(0)

pllmdata=input("select a playlist you have created metadata for: ")
if pllmdata.endswith(".txt"):
    print("loading...")
else:
    pllmdata+=".txt"
    print("loading...")

with open(pllmdata, 'r') as file:
    playlist=file.readlines()

shon=input("shuffle the playlist or play as ordered in the playlist metadata [y/n]: ")

if shon == "y" or shon=="Y":
    random.shuffle(playlist)
os.system('cls' if os.name == 'nt' else 'clear')

async def player():
    for item in playlist:
        print("now playing: ",item,"\ncommands (stop,skip,exit available for 20 seconds after song start)")
        sound=play(item.strip(), async_mode=True)
        process=asyncio.create_task(menu(sound))
        menopt=await process
        if menopt:
            break
        try:
            os.wait()
        except ChildProcessError:
            print(end='')
        os.system('cls' if os.name == 'nt' else 'clear')


asyncio.run(player())
print("looks like you either stopped or the music ended, whatcha gonna do now?")
usin=input("play another playlist(1) or quit(2)")
if usin==1:
    import musik
else:
    exit(0)
