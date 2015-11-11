# coding: utf-8

import pygame.mixer
import sys, time

pygame.mixer.init()
pygame.mixer.music.load('mp3/test01.mp3')
pygame.mixer.music.play(1)

print ("volume: %s" % pygame.mixer.music.get_volume())
print ("time: %s[ms]" % pygame.mixer.music.get_busy())

time.sleep(20)
pygame.mixer.music.stop()
#print "over"