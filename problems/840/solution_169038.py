import math
def bolos (A, B, C):
   """ Esta função calcula o número máximo de bolos que João pode fazer dado os ingredientes que ele possui"""
   bolos = math.floor ( 2/A, 3/B, 5/C)
   return bolos