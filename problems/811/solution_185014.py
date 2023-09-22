def colchao(medidas,H,L):
    '''Funcao que calcula se o colchao vai passar pela porta
    list, int, int -> bool'''
    largura = medidas[2]
    altura = medidas[1]
    if altura > H and largura <= L:
        return True
    elif altura > H and largura > L:
        return False
    elif altura <= H and largura > L:
        return True
    elif altura <= H and largura <= L:
        return True