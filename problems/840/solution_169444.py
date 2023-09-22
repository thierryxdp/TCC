import math  

def bolos(A, B, C):
   """Calcular a quantidade de bolo"""

qtdtrigo(A//2) 
qtdovos(B//3)
qtdleite(C//5)

	return math.min(qtdtrigo, qtdovos, qtdleite)