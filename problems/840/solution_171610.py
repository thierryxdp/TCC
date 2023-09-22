from math import floor
def bolos(A,B,C):
  #Função que determina a quantidade máxima de bolos que João consegue fazer dadas A xícaras de farinha de trigo, B ovos e C colheres de sopas de leite
  return min(floor(A/2), floor(B/3), floor(C/5))