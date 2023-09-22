def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e as dimensões de uma porta,
    retorna se é possível que esse colchão passe pela porta
    list,int,int -> bool'''
    if medidas[0],[1] > H,L or medidas[1],[2] > H,L or medidas[0],[2] > H,L:
        return False
    else:
        return True