def eh_quadrada(matriz):
    '''Esta função identica se a matriz inserida é quadrada ou não.
    list -> bool'''
    
    linhas= len(matriz)
    colunas= len(matriz[0])
    
    if linhas==0 or colunas==0:
        return True
    elif linhas==colunas:
        return True
    else:
        return False