import math
def bolos(farinha, ovos, leite):
"""determina quantos bolos joao pode fazer com a quantidade de ingredientes disponiveis sendo que a farinha e medida em xicaras e o leite em colheres; int, int, int -> int"""
xfarinha = (farinha//2)
novos = (ovos//3)
csleite = (leite//5)
nbolos = min(xfarinha,novos,csleite)
return nbolos