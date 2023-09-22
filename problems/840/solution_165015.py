from math import *
def bolos (A,B,C):
	'''Calcula e retorna a quantidade máxima de possíveis bolos feitos, dado a quantidade de ingredientes 
    (A = Xícaras de farinha de trigo, B = ovos e C = Colheres de sopa de leite)  e considerando que a receita do bolo é
    2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite.
    float, float, float -> float)'''
    
    quantidade = min(floor(A/2), floor(B/3), floor(C/5))
    
    return quantidade