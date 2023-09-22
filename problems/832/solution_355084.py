def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    if matriz==[[]]:
        return True
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    elif nlinhas==ncolunas:
        return True
    else:
        return False