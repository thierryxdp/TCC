def eh_quadrada (matriz):
    """Função que, dada uma matriz, retor um valor booleano True, se for uma matriz quadrada, ou False, caso não seja uma matriz quadrada
    entrada: list
    saída: bool"""
    
    if matriz == [[]] or len(matriz) == len(matriz[0]):
        return True
    
    if len(matriz) != len(matriz[0]):
        return False