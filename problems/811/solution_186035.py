from math import *

def colchao(medidas, H, L):
    '''
    Funcao que indica se o colchao passa pela porta.
    lista, int, int ->

    Uso:
    colchao(medidas, H, L)

    Entrada:
    - medidas (lista, obrigatório): dimensões do colchão
    - H (int, obrigatório): altura da porta em cm
    - L (int, obrigatório): largura da porta em cm

    Saída:
    - Retorna True se o colchão passa pelas portas OU retorna False se não passar. (booleana)
    '''
    if medidas[1] <= H:
        return True
    else:
        return False