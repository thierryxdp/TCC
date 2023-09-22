def colchao (medidas, H, L):
    """Função que, dadas as medidas de um colchão e os valores da altura e da largura de uma porta, calcula se é possível o colchão passar pela abertura da mesma
    entrada: list, int, int
    saída: bool"""
    
    
    if (medidas <= H) and (medidas <= L):
        return True
    
    else:
        return False