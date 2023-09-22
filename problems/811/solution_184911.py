def colchao(medidas,H,L):
    '''Retorna True caso o colchão passe pela porta, False caso contrário
    list, int,int-> bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if H >= B or H >= C:
        return  True
    elif L>= B or L >= C:
        return True
    else:
        return False