import math
def bolos (farinha, ovos, leite):
"""determina a quantidade de bolos que joao pode fazer dadao a quantidade de ingedientes sendo farinha medida em xicaras e leite em colheres de sopa; int, int, int->int)"""
xfarinha=(farinha//2)
novos=(ovos//3)
csleite=(leite//5)
nbolos=min(xfarinha, novos, csleite)
return=nbolos