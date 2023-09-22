def colchao(dimensoes,H,L):
    '''função que dada uma lista com as dimensões de um colchão, ordenadas da
     menor para a maior, e dois números inteiros correspondentes a sua altura(H)
    e largura(l) retorne True se o colchão passar pela porta e False caso nao;
    list, int, int -> bool'''
    if dimensoes[0]<=H and dimensoes[1]<=L:
        return True
    if dimensoes[0]<=H and dimensoes[2]<=L:
        return True
    if dimensoes[1]<=H and dimensoes[2]<=L:
        return True
    if dimensoes[2]<=H and dimensoes[1]<=L:
        return True
    if dimensoes[0]<=L and dimensoes[2]<=H:
        return True
    if dimensoes[0]<=L and dimensoes[1]<=H:
        return True
    else:
        return False