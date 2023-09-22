def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    linhas=1
    colunas=0
    for i in range(nlinhas):
        linhas+=1
        for j in range(ncolunas):
            colunas+=1
    if linhas==colunas:
        return True
    else:
        return False