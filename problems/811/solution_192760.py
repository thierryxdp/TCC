def colchao(medidas,H,L):
    '''função que calcula e retorna se o colchão passará pela porta'''
    medidas.sort()
    
    altura = medidas[0]
    largura = medidas[1]
    comprimento = medidas[2]
    
    if comprimento < H:
        return True
    
    if largura < H:
        return True
    
    if largura < L:
        return True
    
    return False