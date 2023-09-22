def eh_quadrada(matriz):
    '''Esta função identica se a matriz inserida é quadrada ou não.
    list -> bool'''
    
    linhas= len(matriz)
    
    for i in range(linhas):
        colunas= len(matriz[0])
        for j in range(colunas):
            if linhas!=colunas:
                return False
            
    return True