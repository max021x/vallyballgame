import sys
import os
import pygame 
from pygame import mixer
from BgAnimation import Sea
from Player1 import Player1
curdirectory = os.path.dirname(__file__)

pygame.init()
mixer.init()


class Vaollyball:
  def __init__(self) -> None:
    self.width = 1200 
    self.height = 650
    self.fps = 60 
    self.screen = pygame.display.set_mode((self.width,self.height)) 
    self.clock = pygame.time.Clock()
    self.is_active = True
    self.icon_img = pygame.image.load(
    os.path.join(curdirectory , 'graphics' , 'images','iconball.png')
    )
    pygame.display.set_icon(self.icon_img)
    pygame.display.set_caption("ToopBazi")
    # game objects ==== **** ==== 
    self.sea_obj = Sea(self.screen , curdirectory)
    self.music = Music()

  
  def runnig_loop(self):
    self.music.playbg_music()
    
    while self.is_active :
      self.even_loop()
      self.sea_obj.bilt()
      self.sea_obj.animation()
      self.grand = pygame.draw.line( 
        self.screen ,
        (242, 161, 90) 
        ,(0,self.height)
        ,(self.width , self.height)
        ,55
      )
      pygame.display.update()
      self.clock.tick(self.fps) 

  def even_loop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        mixer.quit()
        self.is_active = False 
        sys.exit()


class Music : 
  ocean_bg_sound = mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'ocean.mp3'))
  game_bg_sound = mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'HB.mp3'))
  jump_sound_effect = mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'jump.mp3'))
  ball_bounce = mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'bounce.mp3'))
  win_sound_effect = mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'win0.mp3'))

  channels = []

  for i in range(4):
    channels.append(mixer.Channel(i))
 

  def playbg_music(self):
    # playing backgound music 
    self.channels[0].set_volume(0.5)
    self.channels[1].set_volume(0.2)
    self.channels[0].play(mixer.Sound(self.ocean_bg_sound))
    self.channels[1].play(mixer.Sound(self.game_bg_sound))



def main () :
  Vaollyball().runnig_loop() 


if __name__ == '__main__':
  main()


