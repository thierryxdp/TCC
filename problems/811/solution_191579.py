def colchao(medidas,H,L):
    '''Função que, dada as medidas, a altura (H) e a largura (L),
    retorna 'True' se o colchão passa pela porta e 'False' caso contrário.
    list->bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if H>=A and L>=B:
        return True
    elif H>=B and L>=A:
        return True
    else:
        return False