from math import *
def qtd_divisores(numero):
    '''
    Dado um número inteiro retorna a quantidade de divisores que este número possui.

    Uso:
    qtd_divisores(numero)

    Entrada:
    - número (int): Número inteiro o qual se quer seus divisores

     Saída:
    - Quantidade de divisores de um dado número. (int)
    '''
    qtd=0
    for n in range(1,numero+1):
        if numero%n==0:
            qtd=qtd+1
    return qtd