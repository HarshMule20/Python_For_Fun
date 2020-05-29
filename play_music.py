# import mixer from pygame package
import pygame

# search the music file in the directory
music_file = "dancing_monkey.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
