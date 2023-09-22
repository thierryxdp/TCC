def colchao(medidas,H,L):
    ''' '''
    medidas = [medidas[0], medidas[1], medidas[2]]
    if medidas[1]<=H or L<medidas[2]:
        return True
    else:
        return False