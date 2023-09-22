def eh_quadrada (matriz):
    """Função que, dada uma matriz, retor um valor booleano True, se for uma matriz quadrada, ou False, caso não seja uma matriz quadrada
    entrada: list
    saída: bool"""
    
    if not matriz:
        return True
    
    if len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False