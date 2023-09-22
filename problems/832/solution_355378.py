def eh_quadrada(matriz):
    '''Função que retorna True caso a matriz seja quadrada e False se não for.
    list -> bool'''
    
    i=0
    linhas = len(matriz)
    colunas = len(matriz[i])
   	
    for i in range(linhas):
        if linhas != 0:
        	for i in range(colunas):
                if colunas != 0:
                    return False
                else:
                    return True