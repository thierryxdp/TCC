def eh_quadrada(matriz):
    '''Esta função identica se a matriz inserida é quadrada ou não.
    list -> bool'''
    
    linhas= len(matriz)
    colunas= len(matriz[0])
    
    for i in linhas:
        for j in colunas:
            if linhas==colunas:
        		return True
    		else:
        		return False