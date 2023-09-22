def eh_quadrada(matriz):
    """retorna se a matriz e quadrada ou não
    list(list) -> bool"""
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False
    if len(matriz) = 0
        return True