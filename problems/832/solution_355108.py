def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    lista=[]
    colunas=[]
    for i in range(nlinhas):
        linhas=[]
        for j in range(ncolunas):
            matriz[i][j]=z
            colunas.append(z)
            linhas.append(z)
        lista.append(linhas) 
    if len(lista)==len(colunas):
        return True
    else:
        return False