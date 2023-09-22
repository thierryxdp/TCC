def colchao(medidas,H,L):
    '''Função que, dadas as medidas de um colchão, a altura H e largura L de uma porta, diz se esse colchão passa ou não pela porta; float,float,float,float,float -> bool'''
    if medida[0]>L or medida[1]>H or medida[2]>H:
        return False
    else:
        return True