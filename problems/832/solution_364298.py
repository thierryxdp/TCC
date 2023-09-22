def eh_quadrada(matriz):
    """
    funçao que identifica uma matriz quadrada
    """
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True 
         else:
            return False