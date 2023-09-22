import math
def bolos(A,B,C):
'''Ajudar o João a determinar a quantidade máxima de bolos que consegue fazer'''
qtd_trigo = (A//2)
qtd_ovos = (B//3)
qtd_leite = (C//5)
return min (qtd_trigo,qtd_ovos,qtd_leite)