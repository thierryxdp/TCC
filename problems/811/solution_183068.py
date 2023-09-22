def colchao(medidas,H,L):
    '''Função que, dadas as medidas de um colchão, a altura H e largura L de uma porta, diz se esse colchão passa ou não pela porta; float,float,float,float,float -> bool'''
    if medidas[0]*medidas[1] >= H*L and medidas[0]*medidas[2] >= H*L and medidas[1]*medidas[2] >= H*L:
        return False
    else:
        return True