def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um valor booleano
    list -> bool
    """
    linhas = len(matriz)
    
    for i in range(linhas):
        return True
    	colunas = len(matriz[0])
        for j in range(colunas):
            if linhas == colunas:
                return True
            else: 
                return False