import math
def bolos(A,B,C):
    ''' Entrada:
    		- A(int): número de xícaras de farinha de trigo
            - B(int): número de ovos
            - C(int): número de colheres de sopa de leite
         Saída:
         	qte de bolos com os ingedientes disponíveis'''
    if A//2 >= 1:
        if B//3 >= 1 :
            if C//5 >= 1 :
                return ((A//2),(B//3),(C//5))
    if A//2 <= 0:
        return (0)
    if B//3 <= 0:
        return (0)
    if C//5 <= 0:
        return (0)