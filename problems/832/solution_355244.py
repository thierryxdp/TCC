def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    linha=[]
    coluna=[]
    for m in range(len(matriz)):
        linha.append(m)
        for n in range(len(matriz[0])):
            coluna.append(matriz[m][n])
    nlinhas=len(linha)
    ncoluna=len(coluna)
    if nlinhas==ncoluna:
        return True
    else:
        return False