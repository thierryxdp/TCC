import math
def (A, B ,C):
    '''calcular a quantidade de bolo'''
    
qtd_trigo = math.floor(A/2)
qtd_ovos = math.floor(B/3)
qtd_leite = math.floor(C/5)

 ingrediente = math.min(qtd_trigo, qtd_ovos, qtd_leite)