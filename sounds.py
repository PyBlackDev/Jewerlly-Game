import pygame

pygame.init()

sounds = {"blecch" : pygame.mixer.Sound("media/blecch.ogg"),
          "blecch2" : pygame.mixer.Sound("media/blecch2.ogg"),
          "burn" : pygame.mixer.Sound("media/burn.ogg"),
          "burn_warning" : pygame.mixer.Sound("media/burn_warning.ogg"),
          "burnt" : pygame.mixer.Sound("media/burnt.ogg"),
          "crystal_clear" : pygame.mixer.Sound("media/crystal_clear.ogg"),
          "crystal_clear2" : pygame.mixer.Sound("media/crystal_clear2.ogg"),
          "finished" : pygame.mixer.Sound("media/finished.ogg"),
          "smooth" : pygame.mixer.Sound("media/smooth.ogg"),
          "spicy" : pygame.mixer.Sound("media/spicy.ogg"),
          "swap_down" : pygame.mixer.Sound("media/swap_down.ogg"),
          "swap_up" : pygame.mixer.Sound("media/swap_up.ogg"),
          "options_change" : pygame.mixer.Sound("media/options_change.ogg")}

def play_sound(x):
    pygame.mixer.Sound.play(sounds[x])

def sound_volumes(volume_in):
    for sound in sounds:
        pygame.mixer.Sound.set_volume(sounds[sound], volume_in)