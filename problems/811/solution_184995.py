def colchao(medidas,H,L):
    '''Funcao que calcula se o colchao vai passar pela porta
    list, int, int -> bool'''
    x = medidas[0]*medidas[1]
    if x <= H:
        return True
    else:
        return False