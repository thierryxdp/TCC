from typing import List
def maiores(numeros: List[int], n: int)->int:
    '''dada uma lista de números inteiros e um valor n, 
       retorna todos os números maiores que n'''
    for i in numeros:
        if i > n:
            return list(i)