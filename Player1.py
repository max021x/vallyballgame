import pygame
import os 
from pygame import mixer
pygame.init()
mixer.init()

class Player1:
  def __init__(self , screen , curpath ) -> None:
    self.curpath = curpath
    self.screen = screen 
    self.index = 0
    self.walkimages = []
    self.standimages = []
    self.getImages()
    self.jumpimg = pygame.image.load(
      os.path.join(self.curpath ,
                    'graphics',
                    'player_1',
                    'playerjump.png'
    )).convert_alpha()
    self.surface = pygame.transform.scale2x(pygame.image.load(self.standimages[self.index]).convert_alpha())
    self.player_rect =  self.surface.get_rect(center=(600,545))


  def getImages(self):
    for i in range(2):
      self.standimages.append(
        os.path.join(
          self.curpath ,
          'graphics',
          'player_1' , 
          f'playerstand{i+1}.png'
      ))

    for i in range(3):
      self.walkimages.append(
        os.path.join(
          self.curpath ,
          'graphics',
          'player_1' , 
          f'playerwalk{i+1}.png'
      ))


  def playerStandAnimation(self):
    self.index  += 0.08
    if (self.index >= len(self.standimages)):
      self.index = 0 
    self.surface = pygame.transform.scale2x(pygame.image.load(self.standimages[int(self.index)]).convert_alpha())

  def blit(self):
    self.screen.blit(self.surface , self.player_rect)



