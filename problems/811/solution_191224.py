def colchao(medidas,H,L):
    '''Função que recebe dimensões de um colchão(ALTURA,BASE E COMPRIMENTO) e
    de uma porta e retorna um um valor booleano dizendo se é possível que o
    colchão passe pela porta ou não. list, int, int -> bool'''

    if L > medidas[1] > H:
        return True
    elif medidas[0] > L:
        return False
    elif medidas[1] > H:
        return False
    elif medidas[1] > H:
        return False
    else:
        return True