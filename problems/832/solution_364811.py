def eh_quadrada(matriz):
    """
    	Recebe uma matriz (<matriz>) é retorna se é uma matriz
        quadrada ou não.
        list --> boolean
    """
    linhas = len(matriz)
    colunas = 0
    
    if linhas != 0:
        colunas = len(matriz[0])
        
    if linhas == colunas:
        return True
    else:
        return False