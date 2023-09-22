def eh_quadrada(matriz):
    '''Função que dada uma matriz retoena se essa matriz é
    quadrada ou não
    list->bool'''
    
    linhas=len(matriz)   
    
    if linhas==0:
        return True
        
    colunas=len(matriz[0])
    
    if linhas==colunas:
        return True
        
    else:
        return False