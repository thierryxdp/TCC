def colchao(medidas,H,L):
    '''Funcao que, dadas as medidas de um colchao, a altura (H) e a largura (L) de uma porta, retorna se esse colchão pode passar por ela; list(float, float, float), float, float -> bool'''
    [A,B,C]=medidas
    if (C<H) and (A<L):
        return True
    elif (B<H) and (A<L):
        return True
    elif (C<L) and (A<H):
        return True
    elif (B<L) and (A<H):
        return True 
    elif (C<H) and (B<L):
        return True
    else:
        return False