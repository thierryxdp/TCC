def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    contador=0
    coluna=[]
    for m in range(len(matriz)):
        contador+=1
        for n in range(len(matriz[0])):
            coluna.append(matriz[m][n])
    ncoluna=len(coluna)
    if contador==ncoluna:
        return True
    else:
        return False