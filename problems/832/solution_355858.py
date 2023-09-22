def eh_quadrada (matriz):
    """Função que, dada uma matriz, retorna um valor booleano True para o caso da matriz ser quadrada ou False para o caso da matriz não ser quadrada
    entrada: list
    saída: bool"""
    
    if matriz == [[]] or len(matriz[0]) == len(matriz):
        return True
    if len(matriz[0]) != len(matriz):
        return False