def colchao(medidas,H,L):
    '''Função que, dadas as medidas de um colchão, a altura H e largura L de uma porta, diz se esse colchão passa ou não pela porta; float,float,float,float,float -> bool'''
    if medidas[1]>H and medidas[1]>L:
        return False
    else:
        return True