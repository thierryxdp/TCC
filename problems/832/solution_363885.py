def eh_quadrada (matriz):
    '''função que dada uma matriz retorna se é ou não
    uma matriz quadrada
    list->bool'''
    
    linhas = 0
    colunas = 0
    
    for i in range(len(matriz)):
        linhas += 1
        for j in matriz[0]:
            colunas += 1

    return linhas == colunas