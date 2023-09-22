import math
def qtd_divisores(numero):
    '''função que retorna o número de divisores de um número fornecido como entrada
    int -> int'''
    contagem = 0
    for k in range(1,numero+1):
        if numero % k == 0:
            contagem = contagem + 1
    return contagem