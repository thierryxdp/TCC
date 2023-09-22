def colchao(medidas,H,L):
    '''Funcao que calcula se o colchao vai passar pela porta
    list, int, int -> bool'''
    largura = medidas[2]
    altura = medidas[1]
    if altura <= H:
        return True
    else:
        return False