def colchao (medidas,H,L):
    '''função que as medidas de um colchão
    e de uma porta, retorna se será possível o
    colchão passar na porta'''
    '''list, int -> bool'''
    altura = medidas[0]
    largura = medidas [1]
    comprimento = medidas [2]
    
    if comprimento < H:
        return True
    
    if largura < H:
        return True
    
    if comprimento < L:
        return True
    
    else:
        return False