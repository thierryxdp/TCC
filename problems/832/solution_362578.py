def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um valor booleano
    list -> bool
    """
    linhas = len(matriz)
    if linhas == 0:
    	return True
    else:
        colunas = len(matriz[0])  
    
    for i in range(linhas):
        if linhas == None:
            return True
        for j in range(colunas):
            if colunas == None:
            	return True
            if linhas == colunas:
                return True
            else: 
                return False