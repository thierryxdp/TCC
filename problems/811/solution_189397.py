def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e as dimensões de uma porta,
    retorna se é possível que esse colchão passe pela porta
    list,int,int -> bool'''
    medidas = [medidas]
    if medidas[0:2] > H or medidas[0:2] > L and medidas[1:] > H or medidas[1:] > L:
        return False
    else:
        return True