def eh_quadrada(matriz):
    ''' função que dada uma matriz como parametro retorna um
    bool True caso a matriz seja quadrada
    list->bool'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if linhas==colunas:
                return True
            if linhas==0 and colunas==0:
                return True
    return False