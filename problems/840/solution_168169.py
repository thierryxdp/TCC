from math import *

def bolos (A,B,C):
    '''
    Calcula a quantidade máxima de bolos que João consegue fazer

    Uso (A,B,C)

    Entrada:
    - A (int, obrigatório): número de xícaras de farinha de trigo
    - B (int, obrigatório): número de ovos
    - C (int, obrigatório): número de colheres de sopa de leite

    Saída:
    - Quantidade bolos que João pode realizar (int)
    '''
    if A//2 >= 1:
        if B//3 >= 1:
            if C//5 >= 1:
                return ((A//2)+(B//3)+(C//5)) // 3
    if A//2 <= 0:
        return (0)
    if B//3 <= 0:
        return (0)
    if C//5 <= 0:
        return (0)