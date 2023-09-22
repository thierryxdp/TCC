def bolos(a,b,c):
	'''função que calcule e retorne a quantidade maxima de bolos que João pode fazer'''
# A, B e C indicam, respectivamente, o número de xícaras de farinha de trigo, o número de ovos e o número de colheres de sopa de leite que João tem em casa.
# a proporção da receita é 2:3:5, para farinha, ovo e leite
from math import*
A=round(a/2)  
B=round(b/3)
C=round(c/5)
print (min (A,B,C))