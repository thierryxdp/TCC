def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e as dimensões de uma porta,
    retorna se é possível que esse colchão passe pela porta
    list,int,int -> bool'''
    medidas = [medidas]
    if medidas[0] > H,L and medidas[1] > H,L or medidas[1] > H,L and medidas[2] > H,L or medidas[0] > H,L and medidas[2] > H,L:
        return False
    else:
        return True