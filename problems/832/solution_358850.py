def eh_quadrada(matriz):
    """ 
    Função que recebe uma matriz e retorna se é ou não matriz quadrada
    list -> bool
    
    Parâmetros: 
    Entrada: matriz
    Retorna: True = se for quadrada
    		 False = se não for quadrada
    """
    
    linha = len(matriz)
    if linha == 0:
        return True
    
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    else:
        return False