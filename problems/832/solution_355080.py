def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    if matriz==[[]]:
        return False
    elif nlinhas==ncolunas:
        return True
    else:
        return False