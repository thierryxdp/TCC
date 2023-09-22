def bolos(A,B,C):
	'''função que calcule e retorne a quantidade maxima de bolos que João pode fazer'''
# A, B e C indicam, respectivamente, o número de xícaras de farinha de trigo, o número de ovos e o número de colheres de sopa de leite que João tem em casa.
# a proporção da receita é 2:3:5, para farinha, ovo e leite
from math import*
a= int(A/2)
b= int(B/3)
c= int(C/3)

return floor(a,b,c)