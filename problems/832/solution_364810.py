def eh_quadrada(matriz):
    """
    	Recebe uma matriz (<matriz>) é retorna se é uma matriz
        quadrada ou não.
        list --> boolean
    """
    linhas = len(matriz)
    
    if linhas == 0:
        colunas == 0
    else:
        colunas = len(matriz[0])
        
    if linhas == colunas:
        return True
    else:
        return False