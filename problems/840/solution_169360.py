def bolos(A, B, C):
import math
   """Calcular a quantidade de bolo"""
qtd_trigo = A/2
qtd_ovos = B/3
qtd_leite = C/5

return math.min(qtd_trigo, qtd_ovos, qtd_leite)