import pygame, sys, random
 from pygame.locals import *

 def colisao(rect1, rect2):
 for a, b in [(rect1, rect2), (rect2, rect1)]:

 if ((isPointInsideRect(a.left, a.top, b)) or
 (isPointInsideRect(a.left, a.bottom, b)) or
 (isPointInsideRect(a.right, a.top, b)) or
1
 (isPointInsideRect(a.right, a.bottom, b))):
 return True

 return False