def eh_quadrada (matriz):
    '''função que dada uma matriz retorna se é ou não
    uma matriz quadrada
    list->bool'''
    
    ind = 0
    linhas = 0
    colunas = 0
    
    for i in matriz:
        linhas += 1
        for j in matriz[ind]:
            colunas += 1
        	ind += 1
    
    return linhas == colunas