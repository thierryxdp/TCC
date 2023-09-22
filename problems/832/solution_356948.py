def eh_quadrada(matriz):
    '''Retorna um booleano indicando
       se a matriz de entrada é quadrada
       ou não; matriz->bool'''
    i=len(matriz)-1
    if matriz==[]:
        return True
    for e in matriz:
        linhas=len(matriz)
        colunas=len(matriz[i])
        if linhas==colunas:
            i-=1
        else:
            return False
    return True