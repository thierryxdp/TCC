def colchao(medidas,H,L):
    '''Função que calcula e retorna '''
    
    medidas.sort()
    
    altura = medidas[0]
    largura = medidas[1]
    comprimento = medidas[2]
    
    if largura> L:
        return False
    if largura < L:
        return True
    if comprimento > H:
        return False
    if comprimento < H:
        return True