def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e a altura H e a largura L de uma porta, retorna se o colcão passa ou não pela porta. list,int,int -> bool'''
    len(medidas) == 3
    if medidas[0]*medidas[1] < H*L:
        return True
    elif medidas[1]*medidas[2] < H*L:
        return True
    elif medidas[2]*medidas[0] < H*L:
        return True
    else:
        return False