def eh_quadrada(matriz):
    """Funcao booleana que identifica se uma matriz é quadrada ou nao
    Entrada: list
    Saida: bool
    """
    if len(matriz)== 0:
        return True 
    elif len(matriz[0]) == len(matriz):
        return True 
    else: 
        return False