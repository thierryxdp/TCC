def eh_quadrada(matriz):
    '''Função que dada uma matriz retorna True se essa matriz
    for uma matriz quadrada ou False caso não seja
    list->bool'''
    
    linhas=len(matriz)   
    
    if linhas==0:
        return True
        
    colunas=len(matriz[0])
    
    if linhas==colunas:
        return True
        
    else:
        return False