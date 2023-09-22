import math
def bolos (A, B, C):
   """ Esta função calcula o número máximo de bolos que João pode fazer dado os ingredientes necessários """
   bolos = math.floor (A/2, B/3, C/5)
   return bolos