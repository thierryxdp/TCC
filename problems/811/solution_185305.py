def colchao(medidas,H,L):
    '''Função que calcula e retorna '''
    
    medidas.sort()
    
    altura = [0]
    largura = [1]
    comprimento = [2]
    
    if largura> L:
        return False
    if largura < L:
        return True
    if comprimento > H:
        return False
    if comprimento < H:
        return True