import pygame
from pygame import mixer 
import os 

pygame.init()

class Sea():
  def __init__(self , screen  , curpath):
    self.curpath = curpath
    self.screen = screen    
    self.bg_sea_list = []
    self.fill_list() 
    self.sea_index = 0
    self.sea_surf = self.bg_sea_list[self.sea_index]
    self.sea_rect = self.sea_surf.get_rect(center=(600,340))

  def fill_list (self):
    for i in range(0,31):
      img = pygame.image.load(os.path.join(self.curpath , "graphics\\bg_sea" , "beach"+str(i+1)+'.jpg')).convert_alpha()
      self.bg_sea_list.append(img)


  def animation (self):
    self.sea_index +=0.07
    if self.sea_index >= len(self.bg_sea_list): 
      self.sea_index = 0
    self.sea_surf = self.bg_sea_list[int(self.sea_index)]

  def bilt(self):
    self.screen.blit(self.sea_surf , self.sea_rect)


