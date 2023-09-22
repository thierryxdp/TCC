def colchao (dimensao, H, L):
    '''Função que recebe uma lista com as dimensôes do colchão em centímetros
    além da altura H e da largura L e que em seguida retorna indicando
    se o colchão passa pela porta.
    list, int, int => bool'''
    if (dimensao[0]<=H and dimensao[1]<=L) or (dimensao[0]<=L and dimensao[1]<=H):
        return True
    else:
        return False