def colchao(lista,H,L):
    '''Função que retorna uma lista e um estado das informações ("lista" = list[], "H" e "L) de entrada: list, float, float -> list, boolean"'''
    A = lista[0]
    B = lista[1]

    if (B <= H and A <= L) or (B <=L and A <= H):
        return True
    else:
        return False