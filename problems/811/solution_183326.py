def colchao (A, B, C, H, L):
    """Função que, dadas as medidas de um colchão e os valores da altura e da largura de uma porta, calcula se é possível o colchão passar pela abertura da mesma
    entrada: list, int, int
    saída: bool"""
    
    lista = list(A, B, C)
    
    if (lista [0] <= L and lista[1] <= H and lista[2] <= L):
        return True
    
    elif (lista[0] <= L and [lista[2] <= H and lista[1] <= L):
        return True
    
    else:
        return False