def colchao(medidas, H, L):
    '''Funcao que dadas as medidas A,B e C (em ordem crescente)de um colchão, retornara True caso seja possivel passa-lo pela porta e False caso nao seja.'''
    import math
    if medidas[1]<=math.sqrt(H**2+L**2):
        return True
    if medidas[0]<L and medidas[1]<=H:
        return True 
    elif medidas[0]<L and medidas[1]>=H:
        return False 
    elif medidas[0]>L and medidas[1]<=H:
        return False 
    elif medidas[0]>L and medidas[1]>=H:
        return False
    else:
        return False