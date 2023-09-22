def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    if nlinhas==1 and ncolunas==0:
        return False
    elif nlinhas==ncolunas:
        return True
    else:
        return False