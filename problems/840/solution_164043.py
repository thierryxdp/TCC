def bolos(a,b,c):
	'''função que calcule e retorne a quantidade maxima de bolos que João pode fazer'''
# A, B e C indicam, respectivamente, o número de xícaras de farinha de trigo, o número de ovos e o número de colheres de sopa de leite que João tem em casa.
# a proporção da receita é 2:3:5, para farinha, ovo e leite
    from math import*
    A= a//2  
    B= b//3
    C= c//5
    return min(A,B,C)