import pygame
import os
import time
import random

pygame.mixer.init()

def single(item):
    script_path = os.path.dirname(os.path.abspath(__file__))
    os.system("curl -O https://eyescary-development.github.io/CDN/musik/"+item+".mp3")
    pygame.mixer.music.load(script_path+"/"+item.split("/")[1]+".mp3")
    pygame.mixer.music.play()
    try:
      while True:
        command = input("Enter 'pause', 'resume', or 'stop' (stop works as skip on playlist mode): ").strip().lower()
        if command == 'pause':
            pygame.mixer.music.pause()
        elif command == 'resume':
            pygame.mixer.music.unpause()
        elif command == 'stop':
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid command.")
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
    os.system("rm "+item.split("/")[1]+".mp3")

def playlistmaek():
    loadorno=input("load an (e)xisting playlist or queue up a (n)ew playlist?:")
    if loadorno == "e":
        toload=input("what is the name of the playlist you would like to load?: ")
        file=open(toload+".txt", 'r')
        playlist=file.readlines()
        for item in playlist:
            single(item.strip("\n"))
    else:
        playlist=[]
        while True:
            toap=input("What song do you want to add (write in album/song like ESDP1/AGPM (q to quit)): ")
            if toap == "q":
                break
            else:
                playlist.append(toap)
        for item in playlist:
            single(item)
        saveorno=input("playlist ended, save it?: ")
        if saveorno == "y":
            name=input("give the playlist a name: ")
            file=open(name+".txt", 'w')
            for item in playlist:
                file.write(item+"\n")
            print("saved!")

def main():
  while True:
    playlistorno=input("use or create a playlist? (q to quit): ")
    if playlistorno == "y":
        playlistmaek()
    elif playlistorno == "q":
        quit()
    else:
        single(input("Write song in form of album/song (example ESDP1/AGPM): "))

main()
