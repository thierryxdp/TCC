def colchao (medidas, H, L):
    """Função que, dadas as medidas de um colchão e os valores da altura e da largura de uma porta, calcula se é possível o colchão passar pela abertura da mesma
    entrada: list, int, int
    saída: bool"""
    
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    
    if (a <= H and b <= L) or (a <= L and b <= H) or (b <= H and c <= L) or (b <= L and c <= H) or (a <= H and c <= L) or (a <= L and c <= H):
        return True
    
    else:
        return False