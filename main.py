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
    self.sea_obj = Sea(self.screen)

  
  def runnig_loop(self):

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


def playbg_music():
  # playing backgound music 
  chanel_0 = mixer.Channel(0)
  chanel_1 = mixer.Channel(1)
  chanel_0.set_volume(0.1)
  chanel_1.set_volume(0.5)
  chanel_0.play(mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'HB.mp3')),-1)
  chanel_1.play(mixer.Sound(os.path.join(curdirectory , 'graphics' , 'music' , 'ocean.mp3')),-1)



def main () :
  # playbg_music()
  Vaollyball().runnig_loop() 


if __name__ == '__main__':
  main()


