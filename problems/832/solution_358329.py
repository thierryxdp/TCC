def eh_quadrada(matriz):
    """Função booleana que retorna se uma matriz é quadrática
    int -> bool"""
    for i in matriz:
        if len(matriz) == len(matriz[i]):
            return True
        else:
            return False