def eh_quadrada(matriz):
    """Funcao identifica se uma matriz e quadrada;
    Entrada: list
    Saida: bool"""
    vazio = []
    if matriz!=vazio and len(matriz) == len(matriz[0]) or matriz == vazio:
        return True
   
    else:
        return False