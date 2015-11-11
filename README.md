# naazha

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
// http://brew.sh/

brew install python3
python3 --version

brew install mercurial

brew install git

brew install sdl sdl_image sdl_ttf smpeg portmidi

pip3 install hg+http://bitbucket.org/pygame/pygame

python3
>>> import pygame
>>> pygame.init()
(6, 0)
>>> pygame.display.set_mode((800, 600))
<Surface(800x600x32 SW)>
>>> raise SystemExit

// compile SDL_mixer
http://www.libsdl.org/projects/SDL_mixer/
tar zxvf SDL_mixer-1.2.12.tar.gz
cd SDL_mixer-1.2.12
./configure
make
sudo make install

// sample
import pygame.mixer
import sys, time

pygame.mixer.init()
pygame.mixer.music.load('mp3/test01.mp3')
pygame.mixer.music.play(1)

print ("volume: %s" % pygame.mixer.music.get_volume())
print ("time: %s[ms]" % pygame.mixer.music.get_busy())

time.sleep(20)
pygame.mixer.music.stop()

Good luck!