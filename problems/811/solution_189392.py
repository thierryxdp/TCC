def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e as dimensões de uma porta,
    retorna se é possível que esse colchão passe pela porta
    list,int,int -> bool'''
    medidas = [medidas]
    if (medidas[0] > H and medidas[0] > L) or (medidas[1] > H and medidas[1] > L) or (medidas[2] > H and medidas[2] > L):
        return False
    else:
        return True