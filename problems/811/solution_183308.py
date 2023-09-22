def colchao (A, B, C):
    """Função que, dadas as medidas de um colchão e os valores da altura e da largura de uma porta, calcula se é possível o colchão passar pela abertura da mesma
    entrada: list, int, int
    saída: bool"""
    
    lista_med = list(A, B, C)
    
    if lista_med[1] <= H:
        return True
    
    elif lista_med[1] >= H:
        return False