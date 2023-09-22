def colchao(medidas, H, L):
    '''Funcao que dadas as medidas A,B e C (em ordem crescente)de um colchão, retornara True caso seja possivel passa-lo pela porta e False caso nao seja.'''
    if medidas[0]<L and medidas[1]<H:
        return True 
    if medidas[0]<L and medidas[1]>H:
        return False 
    if medidas[0]>L and medidas[1]<H:
        return False 
    if medidas[0]>L and medidas[1]>H:
        return False