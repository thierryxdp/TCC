from math import *
def total (compras, mercado):
    '''
    Dado um número inteiro positivo N retorna o valor o valor de H com N termos.

    Uso:
   total (compras, mercado)

    Entrada:
    - compras (list): Lista de compras
    - mercado (dicionário): Dicionário contendo os preços

     Saída:
    - Retorna o valor de uma lista de compras(ldc) baseado em um dicionário
    arredondado com 2 casas decimais. (float)
    '''
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)