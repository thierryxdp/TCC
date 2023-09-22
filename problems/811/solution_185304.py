def colchao(medidas,H,L):
    '''Função que calcula e retorna '''
    if min(medidas)> L :
        return False
    if max(medidas) > H:
        return False