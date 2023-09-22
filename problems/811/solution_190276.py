def colchao(medidas,H,L):
    ''' Esta funcao verifica se o colchao vai ou nao passar pela porta'''
    a, b, c = medidas
    if b<=H:
        return True
    elif b<=L:
        return True
    else:
        return False