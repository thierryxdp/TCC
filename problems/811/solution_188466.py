def colchao(medidas,H,L):
    '''Dados uma lista com as dimensões do colchão em
    centímetros, ordenadas da menor para a maior, e dois
    inteiros, correspondentes respectivamente a altura e a
    largura das portas em centímetros.
    list, int, int -> bool'''
    if medidas[0] > L:
        return False
    elif medidas[1] or medidas[2] > H:
        return False
    else:
        return True