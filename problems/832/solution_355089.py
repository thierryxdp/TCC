def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    for i in range(nlinhas):
        for j in range(ncolunas):
    if i==j:
        return True
    else:
        return False