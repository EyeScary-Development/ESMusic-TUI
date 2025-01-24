import pygame
import os
import time

pygame.mixer.init()

def single(item):
    script_path = os.path.dirname(os.path.abspath(__file__))
    os.system("curl -O https://eyescary-development.github.io/CDN/musik/"+item+".mp3")
    pygame.mixer.music.load(script_path+"/"+item.split("/")[1]+".mp3")
    pygame.mixer.music.play()
    try:
      while True:
        command = input("Enter 'pause', 'resume', or 'stop': ").strip().lower()
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

def main():
  while True:
    playlistorno=input("use or create a playlist?: ")
    if playlistorno == "y":
        print("WIP")
    else:
        single(input("Write song in form of album/song (example ESDP1/AGPM): "))

main()
