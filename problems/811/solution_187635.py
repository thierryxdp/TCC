def colchao(medidas,H,L):
    '''Funcao que, dadas as medidas de um colchao, a altura (H) e a largura (L) de uma porta, retorna se esse colchão pode passar por ela; list(float, float, float), float, float -> bool'''
    [A,B,C]=medidas
    if (medidas[2]<H) and (medidas[0]<L):
        return True
    elif (medidas[1]<H) and (medidas[0]<L):
        return True
    elif (medidas[2]<L) and (medidas[0]<H):
        return True
    elif (medidas[1]<L) and (medidas[0]<H):
        return True 
    elif (medidas[2]<H) and (medidas[1]<L):
        return True
    elif (medidas[1]<H) and (medidas[2]<L):
        return True
    else:
        return False