import random
import asyncio
import sys 
import select
import os
from nava import play, stop

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

async def player(playlist):
    for item in playlist:
        print("Now playing:", item, "\nCommands (stop, skip, exit available for 20 seconds after song start)")
        sound = play(item.strip(), async_mode=True)
        process = asyncio.create_task(menu(sound))
        menopt = await process
        if menopt:
            break
        try:
            os.wait()
        except ChildProcessError:
            print(end='')
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Welcome to Musik")

    pllmdata=input("Select a playlist you have created metadata for: ")
    if not pllmdata.endswith(".txt"):
        pllmdata += ".txt"
    print("Loading...")

    with open(pllmdata, 'r') as file:
        playlist=file.readlines()

    shon=input("Shuffle the playlist or play as ordered in the playlist metadata [y/n]: ")

    if shon.lower() == "y":
        random.shuffle(playlist)
    os.system('cls' if os.name == 'nt' else 'clear')


    asyncio.run(player(playlist))
    print("Looks like you either stopped or the music ended, what are you going to do now?")
    usin=input("Play another playlist(1) or quit(2): ")
    if usin == "1":
        pass
    else:
        exit(0)

if __name__ == "__main__":
    while True: main()
