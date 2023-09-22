def colchao(medidas,H,L):
    '''Função que, dadas as medidas de um colchão, a altura H e largura L de uma porta, diz se esse colchão passa ou não pela porta; float,float,float,float,float -> bool'''
    if medidas[0]>L or medidas[1]>H or medidas[2]>H:
        return False
    else:
        return True