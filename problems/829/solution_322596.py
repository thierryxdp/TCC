from math import *
def soma_h(N):
    '''
    Dado um número inteiro positivo N retorna o valor o valor de H com N termos.

    Uso:
    soma_h(N)

    Entrada:
    - número (int): Número de termos de H

     Saída:
    - Retorna o resultado somente com 2 casas decimais. (float)
    '''
    H=0
    for termo in range(1,N+1):
        H=H+1/termo
    return round(H,2)